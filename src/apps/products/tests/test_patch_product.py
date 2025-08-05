from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.products.models import Product

class PatchProductTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Producto Parcial", price=50.00)
        self.url = reverse('products-detail', args=[self.product.id])

    def test_patch_name_only(self):
        response = self.client.patch(self.url, {"name": "Nuevo Nombre"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Nuevo Nombre")

    def test_patch_price_invalid_format(self):
        response = self.client.patch(self.url, {"price": "no-numero"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)

    def test_patch_product_not_found(self):
        url = reverse('products-detail', args=[999])
        response = self.client.patch(url, {"name": "X"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)