from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import PermissionDenied

class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="maxi", password="pass")

    def test_can_list_posts(self):
        maxi = User.objects.get(username="maxi")
        Post.objects.create(owner=maxi, content="test content")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_can_create_post(self):
        self.client.login(username="maxi", password="pass")
        data = {'content': 'This is a new post'}
        response = self.client.post("/posts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.post_maxi = Post.objects.create(owner=self.maxi, content="test content")
        self.post_ben = Post.objects.create(owner=self.ben, content="test content")

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get(f"/posts/{self.post_maxi.id}/")
        self.assertEqual(response.data["content"], "test content")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get("/posts/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_update_post(self):
        self.client.login(username="maxi", password="pass")
        data = {'content': 'This is an updated post'}
        response = self.client.put(f"/posts/{self.post_maxi.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post_maxi.refresh_from_db()
        self.assertEqual(self.post_maxi.content, 'This is an updated post')

    def test_cant_update_post_if_not_owner(self):
        self.client.login(username="ben", password="pass")
        data = {'content': 'This is an updated post'}
        response = self.client.put(f"/posts/{self.post_maxi.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_delete_post(self):
        self.client.login(username="maxi", password="pass")
        response = self.client.delete(f"/posts/{self.post_maxi.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 1)

    def test_cant_delete_post_if_not_owner(self):
        self.client.login(username="ben", password="pass")
        response = self.client.delete(f"/posts/{self.post_maxi.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 2)
