from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):
    def test_create_user_with_email(self):
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["test2@Example.com", "test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
        ]
        password = "testpass123"
        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password=password,
            )

            self.assertEqual(user.email, expected_email)
            self.assertTrue(user.check_password(password))

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email="admin@example.com", password="test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
