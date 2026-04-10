from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


User = get_user_model()


class UserAuthTests(APITestCase):
    def test_signup_creates_user_with_hashed_password(self):
        payload = {
            'username': 'ali',
            'password': 'StrongPass123!',
            'email': 'ali@example.com',
            'first_name': 'Ali',
            'last_name': 'Valiyev',
            'middle_name': 'Bekzodovich',
            'date_of_birth': '2000-01-01',
            'gender': 'male',
            'address': 'Tashkent',
            'position': 'manager',
            'salary': '1500.00',
            'hire_date': '2024-01-10',
        }

        response = self.client.post('/api/v1/users/signup/', payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn('password', response.data)

        user = User.objects.get(username='ali')
        self.assertTrue(user.check_password('StrongPass123!'))

    def test_login_returns_jwt_tokens(self):
        User.objects.create_user(
            username='sardor',
            password='StrongPass123!',
            email='sardor@example.com',
            first_name='Sardor',
            last_name='Karimov',
            middle_name='Anvarovich',
            date_of_birth='1998-05-12',
            gender='male',
            address='Samarkand',
            position='sales',
            salary='2100.00',
            hire_date='2023-08-01',
        )

        response = self.client.post(
            '/api/v1/users/login/',
            {'username': 'sardor', 'password': 'StrongPass123!'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)
