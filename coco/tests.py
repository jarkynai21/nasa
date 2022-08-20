from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *



class TestProductApi(APITestCase):

    @classmethod
    def setUp(cls):
        cls.supplier = Supplier.objects.create(name='Supplier')
        cls.discount = Discount.objects.create(discount=50)
        cls.user = User.objects.create_superuser(email='jaja@gmail.com', password='ymus22')
        cls.category = Category.objects.create(title='Category')

    def test_product_api(self):

        self.client.login(email='jaja@gmail.com', password='ymus22')

        url = '/api/product/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_product_add_api(self):

        self.client.login(email='jaja@gmail.com', password='ymus22')

        url = '/api/product/'

        data = {
            'id': 1,
            'title': 'shop',
            'description': 'dress',
            'creation_date': '18.09.2022, 15:22',
            'price': 1000,
            'picture': 'picture.png',
            'category': '',
            'discount': '',
            'supplier': '',

        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_product_update_api(self):
        self.client.login(email='jaja@gmail.com', password='yumus22')

        url = '/api/product/'

        data = {
            'id': 2,
            'title': 'shop',
            'description': 'dress',
            'creation_date': '18.09.2022, 15:22',
            'price': 1000,
            'picture': 'picture.png',
            'category': '',
            'discount': '',
            'supplier': '',
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_product_delete_api(self):
        self.client.login(email='jaja@gmail.com', password='yumus22')
        self.product = Product.objects.create(title='dssds', id=2, price=12)

        url = '/api/product/2/'

        data = {
            'id': 3,
            'title': 'shop',
            'description': 'dress',
            'creation_date': '18.09.2022, 15:22',
            'price': 1000,
            'picture': 'picture.png',
            'category': '',
            'discount': '',
            'supplier': '',

        }

        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, 204)