from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Follow

class FollowListViewTests(APITestCase):
    """
    Tests for the Follow model list view
    """
    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.follow = Follow.objects.create(follower=self.maxi, following=self.ben)
        self.url = reverse('follow-list')

    def test_can_list_follows(self):
        """
        Test retrieving a list of follow relationships.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_can_create_follow(self):
        """
        Test creating a follow relationship.
        """
        self.client.login(username="ben", password="pass")
        data = {"following": "maxi"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follow.objects.count(), 2)

    def test_cannot_create_duplicate_follow(self):
        """
        Test that duplicate follow relationships are not allowed.
        """
        self.client.login(username="maxi", password="pass")
        data = {"following": "ben"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data["non_field_errors"][0]), "You already are following this user.")


class FollowDetailViewTests(APITestCase):
    """
    Tests for the Follow model detail view
    """
    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.follow = Follow.objects.create(follower=self.maxi, following=self.ben)
        self.url = reverse('follow-detail', args=[self.follow.pk])

    def test_can_retrieve_follow_using_valid_id(self):
        """
        Test retrieving a specific follow relationship.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['follower'], self.follow.follower.username)

    def test_can_delete_own_follow(self):
        """
        Test that a user can delete their own follow relationship.
        """
        self.client.login(username="maxi", password="pass")
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Follow.objects.count(), 0)