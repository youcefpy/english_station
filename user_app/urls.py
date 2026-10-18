from django.urls import path
from django.views.generic import TemplateView

import user_app.views as views  # noqa: PLR0402

urlpatterns = [
    path('verification-info/', TemplateView.as_view(template_name='verification_info.html'),name='verification_info'
    ),
    path('register/',view=views.register_student,name="register_student"),
    path('login/',view=views.login_student,name="login")
]
