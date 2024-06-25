from core.models import Book
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from book.serializers import BookDetailSerializer, BookSerializer

BOOKS_URL = reverse("book:book-list")


def detail_url(book_id: int) -> str:
    return reverse("book:book-detail", args=[book_id])


def create_book(**params):
    defaults = dict(
        title="Sample book",
        author="Test Author",
        description="This is a new book description.",
        isbn="0123456789",
        pages=100,
    )
    defaults.update(params)
    book = Book.objects.create(**defaults)
    return book


class PublicBookAPITests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_list_books(self):
        create_book()
        create_book()

        res = self.client.get(BOOKS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class RegisterBookAPITests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="user@example.com", password="pass123", name="Test User"
        )
        self.client.force_authenticate(self.user)

    def test_list_books(self):
        create_book()
        create_book()

        res = self.client.get(BOOKS_URL)

        books = Book.objects.all().order_by("-id")
        serializer = BookSerializer(books, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_book_detail(self):
        book = create_book()

        res = self.client.get(detail_url(book.id))

        serializer = BookDetailSerializer(book)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_book(self):
        payload = dict(
            title="Sample book",
            author="Test Author",
            description="This is a new book description.",
            isbn="0123456789",
            pages=100,
        )

        res = self.client.post(BOOKS_URL, data=payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        book = Book.objects.get(id=res.data["id"])
        for k, v in payload.items():
            self.assertEqual(getattr(book, k), v)
