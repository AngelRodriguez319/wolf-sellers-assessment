from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.products.models import Product

class DeleteProductTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Eliminar", price=12.00)
        self.url = reverse('products-detail', args=[self.product.id])

    def test_delete_product_success(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_delete_product_not_found(self):
        url = reverse('products-detail', args=[999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)