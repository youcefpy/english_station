import os

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def send_password_setup_email(student, request):
    uid = urlsafe_base64_encode(force_bytes(student.pk))
    token = default_token_generator.make_token(student)

    path = reverse(
        "set_password",
        kwargs={"uidb64": uid, "token": token},
    )
    setup_url = request.build_absolute_uri(path)

    # Send to student.email, from your configured sender.
    # Include setup_url in the message.
    send_mail(
        subject="Validate Registration",
        message=(
            f"Hello,{student.first_name}\n"
            f"We juste confirmed your information click on the"
            "link bellow to confirm your information and set your password"
            f"{setup_url}"
        ),
        from_email= os.getenv(key="EMAIL_HOST_USER"),
        recipient_list = [
            student.email
        ],
    )
