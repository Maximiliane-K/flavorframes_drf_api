from django.urls import path
from bookmarks import views

urlpatterns = [
    path("bookmarks/", views.BookmarkListCreateView.as_view(), name="bookmark-list"),
    path("bookmarks/<int:pk>/", views.BookmarkDetailView.as_view(), name="bookmark-detail"),
]
