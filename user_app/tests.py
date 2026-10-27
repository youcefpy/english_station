from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import Student


class TestRegistrationStudent(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Student_first_name",
            last_name="student_last_name",
            email="toto@email.com",
            username="toto@email.com",
            level=1,
            stream="common_core_st",
            is_active=False,
        )

    @patch("user_app.views.send_mail")
    def test_send_email_after_registration(self, mock_send_mail):
        response = self.client.post(
            reverse("register_student"),
            {
                "first_name": "New",
                "last_name": "Student",
                "email": "new.student@email.com",
                "level": "1",
                "stream": "common_core_st",
            },
        )

        self.assertRedirects(response, reverse("verification_info"))
        student = Student.objects.get(email="new.student@email.com")
        self.assertEqual(student.username, student.email)
        self.assertFalse(student.is_active)
        self.assertFalse(student.has_usable_password())
        mock_send_mail.assert_called_once()
        self.assertEqual(mock_send_mail.call_args.kwargs["subject"], "Validation email")
        self.assertEqual(mock_send_mail.call_args.kwargs["from_email"], student.email)

    @patch("user_app.views.send_password_setup_email")
    def test_validation_student_by_admin(self, mock_send_setup_email):
        admin = get_user_model().objects.create_user(
            username="admin", password="admin-password", is_staff=True
        )
        self.client.force_login(admin)

        response = self.client.post(
            reverse("approve_student", args=[self.student.pk])
        )

        self.assertRedirects(response, reverse("admin_panel"))
        self.student.refresh_from_db()
        self.assertTrue(self.student.is_active)
        mock_send_setup_email.assert_called_once_with(self.student, response.wsgi_request)

    def test_set_password_student(self):
        uidb64 = urlsafe_base64_encode(force_bytes(self.student.pk))
        token = default_token_generator.make_token(self.student)

        response = self.client.post(
            reverse("set_password", kwargs={"uidb64": uidb64, "token": token}),
            {"password": "StrongPassword123!", "confirm_password": "StrongPassword123!"},
        )

        self.assertRedirects(response, reverse("login"))
        self.student.refresh_from_db()
        self.assertTrue(self.student.check_password("StrongPassword123!"))

    @patch("user_app.views.send_mail")
    def test_invalid_registration_does_not_create_student_or_send_email(self, mock_send_mail):
        response = self.client.post(
            reverse("register_student"),
            {
                "first_name": "Invalid",
                "last_name": "Student",
                "email": "not-an-email",
                "level": "1",
                "stream": "common_core_st",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.count(), 1)
        mock_send_mail.assert_not_called()
