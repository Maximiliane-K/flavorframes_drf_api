from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile

class ProfileListViewTests(APITestCase):
    """
    Tests for the Profile model list view
    """

    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.profile_maxi = Profile.objects.get(owner=self.maxi)
        self.profile_ben = Profile.objects.get(owner=self.ben)
        self.url = reverse('profile-list')

    def test_can_list_profiles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_cannot_list_profiles_when_not_logged_in(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class ProfileDetailViewTests(APITestCase):
    """
    Tests for the Profile model detail view
    """

    def setUp(self):
        self.maxi = User.objects.create_user(username="maxi", password="pass")
        self.ben = User.objects.create_user(username="ben", password="pass")
        self.profile_maxi = Profile.objects.get(owner=self.maxi)
        self.profile_ben = Profile.objects.get(owner=self.ben)
        self.url_maxi = reverse('profile-detail', args=[self.profile_maxi.pk])
        self.url_ben = reverse('profile-detail', args=[self.profile_ben.pk])

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get(self.url_maxi)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['owner'], self.profile_maxi.owner.username)

    def test_cannot_retrieve_profile_using_invalid_id(self):
        response = self.client.get(reverse('profile-detail', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_delete_own_profile(self):
        self.client.login(username="maxi", password="pass")
        response = self.client.delete(self.url_maxi)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profile.objects.filter(id=self.profile_maxi.id).count(), 0)

    def test_cannot_delete_other_profile(self):
        self.client.login(username="ben", password="pass")
        response = self.client.delete(self.url_maxi)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Profile.objects.filter(id=self.profile_maxi.id).count(), 1)
