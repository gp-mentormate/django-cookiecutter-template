from django.contrib.auth import get_user_model
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase


class UserRegistrationTest(APITestCase):
    def setUp(self):
        self.fake = Faker()
        self.register_url = reverse("customuser-list")

    def test_user_registration(self):
        # Arrange
        # Prepare data for registration
        user_data = {
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": self.fake.password(),
        }

        # Act
        # Make a POST request to register a new user
        response = self.client.post(self.register_url, user_data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)

        self.assertEqual(response.data["username"], user_data["username"])
        self.assertEqual(response.data["email"], user_data["email"])
        self.assertTrue("password" not in response.data)

    def test_user_registration_existing_username(self):
        # Arrange
        user_data = {
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": self.fake.password(),
        }

        # Create a user with the same username
        get_user_model().objects.create_user(**user_data)

        # Act
        response = self.client.post(self.register_url, user_data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("username", response.data)
        self.assertIn("A user with that username already exists.",
                      response.data["username"])
