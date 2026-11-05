"""
URL configuration for project_english project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

import app_english.views as views  # noqa: PLR0402

urlpatterns = [
    path('', views.index, name="index"),
    path('check-info-student/',views.check_information_student_view,name='check-student-sigup'),
    path('units/',views.unit_view,name='units'),
    path('streams/<int:stream_id>/semesters/', views.semester_view, name='semesters_by_stream'),
    path('streams/<int:stream_id>/semesters/<int:semester>/units/', views.unit_view, name='units_by_semester'),
    path('streams/<int:level>/', views.stream_view, name='streams_by_level'),
    path('cours/<int:cours_id>',views.cours_view, name="cours")
]


