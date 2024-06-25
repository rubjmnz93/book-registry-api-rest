from core.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author"]
        read_only_fields = ["id"]


class BookDetailSerializer(BookSerializer):
    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields + ["description", "isbn", "pages"]
