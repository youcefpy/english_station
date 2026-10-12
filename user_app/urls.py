from django.urls import path

import user_app.views as views

urlpatterns = [
    path('register/',view=views.register_student,name="register_student")
]
