from django.contrib.auth.models import User
from posts.models import Post
from bookmarks.models import Bookmark
from rest_framework import status
from rest_framework.test import APITestCase

class BookmarkListViewTests(APITestCase):
    """
    Test for the Bookmarks model list view
    """
    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.post = Post.objects.create(owner=self.ben, content="test content")
        Bookmark.objects.create(owner=self.maxi, post=self.post)

    def test_can_list_bookmarks(self):
        self.client.login(username="maxi", password="pass")
        response = self.client.get("/bookmarks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_cant_list_bookmarks_when_not_logged_in(self):
        response = self.client.get("/bookmarks/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BookmarkDetailViewTests(APITestCase):
    def setUp(self):
        """
        Tests for the Bookmarks model detail view
        """
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.post = Post.objects.create(owner=self.ben, content="test content")
        self.bookmark = Bookmark.objects.create(owner=self.maxi, post=self.post)
        self.detail_url = f"/bookmarks/{self.bookmark.id}/"

    def test_can_retrieve_bookmark(self):
        self.client.login(username="maxi", password="pass")
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["post"]["content"], "test content")

    def test_cant_retrieve_bookmark_if_not_owner(self):
        self.client.login(username="ben", password="pass")
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_delete_bookmark(self):
        self.client.login(username="maxi", password="pass")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bookmark.objects.count(), 0)

    def test_cant_delete_bookmark_if_not_owner(self):
        self.client.login(username="ben", password="pass")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Bookmark.objects.count(), 1)
