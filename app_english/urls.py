from django.urls import path

import app_english.views as views  # noqa: PLR0402

urlpatterns = [
    path('', views.index, name="index"),
    path('check-info-student/',views.check_information_student_view,name='check-student-sigup'),
    path('units/',views.unit_view,name='units'),
    path('streams/<int:level>/', views.stream_view, name='streams_by_level'),
    path('cours/<int:cours_id>',views.cours_view, name="cours"),

    path('streams/',views.StreamList.as_view())
]


