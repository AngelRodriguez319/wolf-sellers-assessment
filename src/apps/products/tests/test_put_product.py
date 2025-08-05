from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.products.models import Product

class PutProductTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Producto Original", price=15.00)
        self.url = reverse('products-detail', args=[self.product.id])

    def test_put_product_success(self):
        data = {
            "name": "Producto Actualizado",
            "description": "Actualización completa",
            "price": "30.00",
            "available": False
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, data['name'])
        self.assertEqual(str(self.product.price), data['price'])
        self.assertEqual(self.product.description, data['description'])
        self.assertEqual(self.product.available, data['available'])

    def test_put_missing_required_field(self):
        data = {
            "price": "30.00",
            "available": True
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_product_invalid_price_format(self):
        data = {
            "name": "Nombre",
            "price": "invalido",
            "available": True
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)   

    def test_put_product_not_found(self):
        url = reverse('products-detail', args=[999])
        response = self.client.put(url, {"name": "X"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)