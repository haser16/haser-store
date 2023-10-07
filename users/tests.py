from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


# Login test
class UserLoginViewTestCase(TestCase):

    def test_view(self):
        path = reverse('users:login')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Login')


# Registration test
class UserRegistrationViewTestCase(TestCase):

    def test_view(self):
        path = reverse('users:registration')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Registration')


# Rules test
class RulesTemplateViewTestCase(TestCase):

    def test_view(self):
        path = reverse('users:rules')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Rules')
