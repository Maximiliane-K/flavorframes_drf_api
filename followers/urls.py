from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowList.as_view(), name='follow-list'),
    path('followers/<int:pk>/', views.FollowDetail.as_view(), name='follow-detail'),
]
