from core.models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from book import serializers


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookDetailSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.all().order_by("-id")

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.BookSerializer

        return self.serializer_class
