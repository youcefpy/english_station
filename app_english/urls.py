from django.urls import include, path
from rest_framework.routers import DefaultRouter

import app_english.views as views  # noqa: PLR0402

router = DefaultRouter()
router.register('units',views.UnitViewSet,basename="unit")
router.register('streams',views.StreamViewSet,basename="stream")
router.register('cours',views.CoursViewSet,basename='cours')

urlpatterns = [
    path('', views.index, name="index"),
    path('check-info-student/',views.check_information_student_view,name='check-student-sigup'),
    path('units/',views.unit_view,name='units'),
    path('streams/<int:level>/', views.stream_view, name='streams_by_level'),
    path('cours/<int:cours_id>',views.cours_view, name="cours"),

    #######################################
    ## API ROUTES
    ########################
    path("api/", include(router.urls)),
]
