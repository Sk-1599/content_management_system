from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import ContentItem, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testauthor',   
            'email': 'author@test.com',
            'password': 'TestPass123',
            'full_name': 'Test Author',
            'phone': '1234567890',
            'pincode': '123456',
            'is_author': True
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_registration(self):
        response = self.client.post('/api/register/', self.user_data)
        print("User registration",response,response.status_code)
        return response
    
    def test_user_login(self):
        response = self.client.post('/api/login/', {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        })
        print("User login",response,response.status_code)
        return response.status_code

class ContentItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testauthor',
            email='author@test.com',
            password='TestPass123',
            full_name='Test Author',
            phone='1234567890',
            pincode='123456',
            is_author=True
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='Test Category')
        self.content_data = {
            'title': 'Test Content',
            'body': 'Test Body',
            'summary': 'Test Summary',
            'document': SimpleUploadedFile('new_test_document.pdf', BytesIO(b"New test file content").read()),
            'categories': [self.category.id]
        }

    def test_content_creation(self):
        response = self.client.post('/api/contents/', self.content_data)
        return response.status_code

    def test_content_retrieval(self):
        content = ContentItem.objects.create(
            author=self.user, 
            title='Test Content',
            body='Test Body',
            summary='Test Summary',
            document=SimpleUploadedFile('new_test_document.pdf', BytesIO(b"New test file content").read())
        )
        content.categories.set([self.category])
        response = self.client.get(f'/api/contents/{content.id}/')
        return response.status_code
