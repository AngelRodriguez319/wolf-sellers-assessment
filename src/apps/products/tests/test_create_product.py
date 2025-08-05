from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.products.models import Product

class CreateProductTest(APITestCase):

    def setUp(self):
        self.url = reverse('products-list')

    def test_create_product_success(self):
        data = {
            "name": "Nuevo producto",
            "description": "Un producto de prueba",
            "price": "19.99",
            "available": False
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

        product = Product.objects.first()
        self.assertEqual(product.name, data['name'])
        self.assertEqual(product.description, data['description'])
        self.assertEqual(str(product.price), data['price'])
        self.assertEqual(product.available, data['available'])

    def test_create_product_without_optional_fields(self):
        data = {
            "name": "Producto sin descripción",
            "price": "50.00"
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        product = Product.objects.first()
        self.assertEqual(product.name, data['name'])
        self.assertIsNone(product.description)
        self.assertEqual(str(product.price), data['price'])
        self.assertTrue(product.available)

    def test_create_product_missing_required_field(self):
        data = {
            "description": "Falta el nombre",
            "price": "25.00"
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_invalid_price_format(self):
        data = {
            "name": "Producto inválido",
            "price": "texto",
            "available": True
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)
