from django.urls import path
from .views import EventAttendanceViewSet

urlpatterns = [
    path('attendance/', EventAttendanceViewSet.as_view({'get': 'list', 'post': 'create'}), name='attendance-list'),
    path('attendance/<int:event_id>/', EventAttendanceViewSet.as_view({'delete': 'destroy'}), name='attendance-detail'),
]