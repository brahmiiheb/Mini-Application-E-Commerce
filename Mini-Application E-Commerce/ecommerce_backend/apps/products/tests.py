# products/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductTests(APITestCase):
    def test_create_product(self):
        url = '/products/create/'
        data = {'name': 'Test Product', 'price': 10.0, 'stock': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_get_products(self):
        url = '/products/'
        product = Product.objects.create(name='Test Product', price=10.0, stock=100)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_product(self):
        product = Product.objects.create(name='Test Product', price=10.0, stock=100)
        url = f'/products/{product.id}/update/'
        data = {'name': 'Updated Product', 'price': 15.0, 'stock': 150}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.name, 'Updated Product')

    def test_delete_product(self):
        product = Product.objects.create(name='Test Product', price=10.0, stock=100)
        url = f'/products/{product.id}/delete/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_filter_in_stock(self):
        product_in_stock = Product.objects.create(name='In Stock Product', price=20.0, stock=100)
        product_out_of_stock = Product.objects.create(name='Out of Stock Product', price=20.0, stock=0)
        url = '/products/?in_stock=true'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'In Stock Product')
