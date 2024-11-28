from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from likes.models import Like
from posts.models import Post

class LikeListViewTests(APITestCase):
    """
    Tests for the Like model list view
    """
    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.post = Post.objects.create(owner=self.maxi, content="Maxi's post content")
        self.url = reverse('like-list')

    def test_can_list_likes(self):
        Like.objects.create(user=self.maxi, post=self.post)
        self.client.login(username="maxi", password="pass")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_cannot_create_like_when_not_logged_in(self):
        data = {'post': self.post.id}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeDetailViewTests(APITestCase):
    """
    Tests for the Like model detail view
    """
    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.post = Post.objects.create(owner=self.maxi, content="Maxi's post content")
        self.like = Like.objects.create(user=self.maxi, post=self.post)
        self.url = reverse('like-detail', args=[self.like.id])

    def test_can_retrieve_like_using_valid_id(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], self.like.user.username)

    def test_cant_retrieve_like_using_invalid_id(self):
        response = self.client.get(reverse('like-detail', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_delete_like(self):
        self.client.login(username="maxi", password="pass")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Like.objects.filter(id=self.like.id).count(), 0)
