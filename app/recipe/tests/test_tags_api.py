from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag, Recipe

from recipe import serializers

TAGS_URL = reverse('recipe:tag-list')


class PublicTagsApiTests(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        
    def test_login_required(self):
        response = self.client.get(TAGS_URL)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        
class PrivateTagsApiTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'josekangethe2@gmail.com',
            'test@123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        
    def test_retrieve_tags(self):
        Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=self.user, name='Desert')
        
        response = self.client.get(TAGS_URL)
        
        tags = Tag.objects.all().order_by('-name')
        serializer = serializers.TagSerializer(tags, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
    def test_tags_limited_to_user(self):
        user2 = get_user_model().objects.create_user(
            'other@gmail.com',
            'other123'
        )
        Tag.objects.create(user=user2, name='other')
        tag = Tag.objects.create(user=self.user, name="other food")
        
        response = self.client.get(TAGS_URL)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], tag.name)
        
    def test_create_tag_successful(self):
        payload = {'name': "Test"}
        self.client.post(TAGS_URL, payload)
        
        exists = Tag.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()
        self.assertTrue(exists)
        
    def test_create_tag_inavlid(self):
        payload = {'name': ''}
        response = self.client.post(TAGS_URL, payload)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_retrieve_tags_assigned_to_recipes(self):
        tag1 = Tag.objects.create(user=self.user, name='Breakfast')
        tag2 = Tag.objects.create(user=self.user, name='Lunch')
        recipe = Recipe.objects.create(
            title='Coriander eggs on toast',
            time_minutes=10,
            price=5.00,
            user=self.user
        )
        recipe.tags.add(tag1)
        
        response = self.client.get(TAGS_URL, {'assigned_only': 1})
        
        serializer1 = serializers.TagSerializer(tag1)
        serializer2 = serializers.TagSerializer(tag2)
        self.assertIn(serializer1.data, response.data)
        self.assertNotIn(serializer2.data, response.data)
        
    def test_retrieve_tags_assigned_unique(self):
        tag = Tag.objects.create(user=self.user, name='Breakfast')
        Tag.objects.create(user=self.user, name='Lunch')
        recipe1 = Recipe.objects.create(
            title='Puncakes',
            time_minutes=3,
            price=2.00,
            user=self.user
        )
        recipe1.tags.add(tag)
        recipe2 = Recipe.objects.create(
            title='Porridge',
            time_minutes=3,
            price=2.00,
            user=self.user
        )
        recipe2.tags.add(tag)
        
        response = self.client.get(TAGS_URL, {'assigned_only': 1})
        
        self.assertEqual(len(response.data), 1)
        
        
