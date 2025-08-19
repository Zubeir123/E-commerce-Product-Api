from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Product


class ProductApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='StrongPass123')
        self.login_url = reverse('token_obtain')
        self.list_url = reverse('product-list')

def auth(self):
    res = self.client.post(self.login_url, {'username':'alice','password':'StrongPass123'}, format='json')
    token = res.data['access']
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

def test_public_can_list_products(self):
    Product.objects.create(name='Book', description='x', price=10, category='books', stock=3)
    res = self.client.get(self.list_url)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(res.data['count'], 1)

def test_authenticated_can_create_product(self):
    self.auth()
    payload = {"name":"Pen","description":"Blue","price":"1.50","category":"stationery","stock":100}
    res = self.client.post(self.list_url, payload, format='json')
    self.assertEqual(res.status_code, 201)

def test_search_endpoint(self):
    Product.objects.create(name='iPhone 14', description='smartphone', price=999, category='electronics', stock=5)
    res = self.client.get(self.list_url + 'search/?q=iphone')
    self.assertEqual(res.status_code, 200)
    self.assertGreaterEqual(res.data['count'], 1)
