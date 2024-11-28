from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from posts.models import Post

class CommentListViewTests(APITestCase):
    """
    Tests for the Comment model list view
    """
    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.post = Post.objects.create(owner=self.maxi, content="A post content")
        self.url = reverse('comment-list')

    def test_can_list_comments(self):
        Comment.objects.create(owner=self.maxi, post=self.post, content="A comment")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class CommentDetailViewTests(APITestCase):
    """
    Tests for the Comment model detail view
    """
    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.post_maxi = Post.objects.create(owner=self.maxi, content="Maxi's post content")
        self.post_ben = Post.objects.create(owner=self.ben, content="Ben's post content")
        self.comment_maxi = Comment.objects.create(owner=self.maxi, post=self.post_maxi, content="Maxi's comment")
        self.comment_ben = Comment.objects.create(owner=self.ben, post=self.post_ben, content="Ben's comment")
        self.url_maxi = reverse('comment-detail', args=[self.comment_maxi.id])

    def test_can_retrieve_comment_using_valid_id(self):
        response = self.client.get(self.url_maxi)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.comment_maxi.content)

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get(reverse('comment-detail', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_update_comment(self):
        self.client.login(username="maxi", password="pass")
        data = {'content': 'Updated comment content'}
        response = self.client.put(self.url_maxi, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment_maxi.refresh_from_db()
        self.assertEqual(self.comment_maxi.content, 'Updated comment content')

    def test_cant_update_comment_if_not_owner(self):
        self.client.login(username="ben", password="pass")
        data = {'content': 'Ben trying to update Maxi’s comment'}
        response = self.client.put(self.url_maxi, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_delete_comment(self):
        self.client.login(username="maxi", password="pass")
        response = self.client.delete(self.url_maxi)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.filter(id=self.comment_maxi.id).count(), 0)

    def test_cant_delete_comment_if_not_owner(self):
        self.client.login(username="ben", password="pass")
        response = self.client.delete(self.url_maxi)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Comment.objects.filter(id=self.comment_maxi.id).count(), 1)
