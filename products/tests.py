from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


# Index test
class IndexTemplateViewTestCase(TestCase):

    def test_view(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Haser-Store')
