from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.products.models import Product

class GetProductListTest(APITestCase):

    def setUp(self):
        self.url = reverse('products-list')
        for i in range(60):
            Product.objects.create(name=f"Producto {i+1}", price=10.00 + i)

    def test_list_products_paginated_default(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('count', response.data)
        self.assertIn('page', response.data)
        self.assertIn('per_page', response.data)
        self.assertIn('results', response.data)

        self.assertEqual(response.data['count'], 60)
        self.assertEqual(response.data['page'], 1)
        self.assertEqual(response.data['per_page'], 50)
        self.assertEqual(len(response.data['results']), 50)

    def test_list_products_paginated_custom_per_page(self):
        response = self.client.get(self.url, {'per_page': 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 60)
        self.assertEqual(response.data['page'], 1)
        self.assertEqual(response.data['per_page'], 10)
        self.assertEqual(len(response.data['results']), 10)

    def test_list_products_second_page(self):
        response = self.client.get(self.url, {'page': 2, 'per_page': 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 60)
        self.assertEqual(response.data['page'], 2)
        self.assertEqual(response.data['per_page'], 10)
        self.assertEqual(len(response.data['results']), 10)

    def test_list_products_invalid_page(self):
        response = self.client.get(self.url, {'page': 100})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
