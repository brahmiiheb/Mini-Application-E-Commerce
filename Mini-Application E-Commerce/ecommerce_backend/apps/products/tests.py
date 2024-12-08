from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductTests(APITestCase):

    def test_create_product(self):
        # Valid product creation
        url = 'http://127.0.0.1:8000/api/products/create/'
        data = {'name': 'Test Product','description' : 'description ', 'price': 10.0, 'stock': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_create_product_missing_name(self):
        # Test missing product name
        url = 'http://127.0.0.1:8000/api/products/create/'
        data = {'price': 10.0, 'stock': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_create_product_invalid_price(self):
        # Test invalid price (string instead of number)
        url = 'http://127.0.0.1:8000/api/products/create/'
        data = {'name': 'Test Product', 'price': 'invalid', 'stock': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)

    def test_create_product_negative_price(self):
        # Test negative price
        url = 'http://127.0.0.1:8000/api/products/create/'
        data = {'name': 'Test Product', 'price': -10.0, 'stock': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)

    def test_create_product_negative_stock(self):
        # Test negative stock
        url = 'http://127.0.0.1:8000/api/products/create/'
        data = {'name': 'Test Product', 'price': 10.0, 'stock': -1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('stock', response.data)

    def test_create_product_missing_price(self):
        # Test missing price
        url = 'http://127.0.0.1:8000/api/products/create/'
        data = {'name': 'Test Product', 'stock': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)

    def test_create_product_missing_stock(self):
        # Test missing stock
        url = 'http://127.0.0.1:8000/api/products/create/'
        data = {'name': 'Test Product', 'price': 10.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('stock', response.data)

    def test_get_products(self):
        # Test listing products
        url = 'http://127.0.0.1:8000/api/products/'
        product = Product.objects.create(name='Test Product', price=10.0, stock=100)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_product(self):
        product = Product.objects.create(name='Test Product', price=10.0, stock=100)
        url = f'http://127.0.0.1:8000/api/products/{product.id}/update/'
        data = {'name': 'Updated Product', 'price': 15.0, 'stock': 150}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.name, 'Updated Product')

    def test_delete_product(self):
        product = Product.objects.create(name='Test Product', price=10.0, stock=100)
        url = f'http://127.0.0.1:8000/api/products/{product.id}/delete/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_filter_in_stock(self):
        product_in_stock = Product.objects.create(name='In Stock Product', price=20.0, stock=100)
        product_out_of_stock = Product.objects.create(name='Out of Stock Product', price=20.0, stock=0)
        url = 'http://127.0.0.1:8000/api/products/?in_stock=true'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'In Stock Product')
