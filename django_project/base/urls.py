from django.urls import path, include

from rest_framework.routers import DefaultRouter

from base.views import (
    BookViewset,
    BookAuthorViewset,
    BookGenreViewset,
    BookLanguageViewset
)

router = DefaultRouter()
router.register(r'books', BookViewset, basename='book')
router.register(r'book-authors', BookAuthorViewset, basename='book-author')
router.register(r'book-genres', BookGenreViewset, basename='book-genre')
router.register(r'book-languages', BookLanguageViewset, basename='book-language')  # NOQA

urlpatterns = [
    path('', include(router.urls)),
]
