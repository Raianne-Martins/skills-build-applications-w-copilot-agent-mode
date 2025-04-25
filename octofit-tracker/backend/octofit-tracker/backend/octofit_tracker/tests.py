from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }

    def test_create_user(self):
        response = self.client.post('/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        self.client.post('/users/', self.user_data, format='json')
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

# Similar test cases can be added for Team, Activity, Leaderboard, and Workouts