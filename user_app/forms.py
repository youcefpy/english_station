from django import forms
from django.forms import ModelForm

from .models import Admin, Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','email','level','stream']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-select" if isinstance(
                field.widget, forms.Select
            ) else "form-control"

class StudentFormSetPassWord(ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm password"
    )
    class Meta:
        model= Student
        fields = ['password']

        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            }

    def clean(self):
        cleaned_data = super().clean()
        assert cleaned_data
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

class AdminForm(ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'


class StudentLogin(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=255,
        widget=forms.EmailInput(attrs={
            "placeholder": "student@email.com",
            "class": "form-control",
        }),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
