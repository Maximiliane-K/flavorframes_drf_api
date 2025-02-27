from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventAttendanceViewSet

router = DefaultRouter()
router.register(r"event-attendance", EventAttendanceViewSet, basename="event-attendance")

urlpatterns = [
    path("", include(router.urls)),
]
