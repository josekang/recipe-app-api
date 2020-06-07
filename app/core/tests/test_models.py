from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_eamail(self):
        
        email = "josekangethe2@gmail.com"
        password = "Test@123"
            
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normalize(self):
        email = "josekangethe2@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test@123')
        
        self.assertEqual(user.email, email.lower())
        
    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")
            
    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser(
            "test@test.com",
            "test123"
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)