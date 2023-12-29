from rest_framework import viewsets, permissions

from base.models import Book, BookAuthor, BookGenre, BookLanguage
from base.serializers import (
    BookSerializer,
    BookAuthorSerializer,
    BookGenreSerializer,
    BookLanguageSerializer
)


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny,]


class BookAuthorViewset(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
    permission_classes = [permissions.AllowAny,]


class BookGenreViewset(viewsets.ModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    permission_classes = [permissions.AllowAny,]


class BookLanguageViewset(viewsets.ModelViewSet):
    queryset = BookLanguage.objects.all()
    serializer_class = BookLanguageSerializer
    permission_classes = [permissions.AllowAny,]
