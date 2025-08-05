from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.products.models import Product

class GetProductDetailTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Detalle Producto", price=99.99, description="Descripción del producto", available=False)
        self.url = reverse('products-detail', args=[self.product.id])

    def test_retrieve_product_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)
        self.assertEqual(str(response.data['price']), str(self.product.price))
        self.assertEqual(response.data['description'], self.product.description)
        self.assertEqual(response.data['available'], self.product.available)

    def test_retrieve_product_not_found(self):
        invalid_url = reverse('products-detail', args=[999])
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)