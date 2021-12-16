from django.test import TestCase
from django.test.client import Client
from authapp.models import ShopUser


class AuthUserTestCase(TestCase):
    status_ok = 200
    status_redirect = 302
    username = 'django'
    password = 'geekbrains'

    def setUp(self) -> None:
        self.client = Client()

        self.superuser = ShopUser.objects.create_superuser(
            username=self.username,
            password=self.password,
        )

    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_ok)
        self.assertTrue(response.context['user'].is_anonymous)
        self.client.login(username=self.username, password=self.password)

        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, self.status_ok)
        self.assertFalse(response.context['user'].is_anonymous)

    def test_user_register(self):
        response = self.client.get('/auth/register/')
        self.assertEqual(response.status_code, self.status_ok)
        self.assertTrue(response.context['user'].is_anonymous)

        new_user = {
            'username': 'Пользователь_2',
            'first_name': 'Пол_2',
            'last_name': 'Пол_2',
            'password1': 'geekbrains',
            'password2': 'geekbrains',
            'email': 'polz@geekshop.local',
            'age': '30'}

        response = self.client.post('/auth/register/', data=new_user)
        self.assertEqual(response.status_code, self.status_redirect)

