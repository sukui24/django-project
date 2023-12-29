from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from base.tests.fixture import create_book
from base.models import BookGenre, BookAuthor, BookLanguage


class TestBook(TestCase):
    """
    Test Book urls
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.list_books_path = reverse('book-list')
        self.retrieve_book_path = reverse('book-detail', args=[1])

    def test_get_books(self):

        response = self.client.get(self.list_books_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        book = create_book()

        response = self.client.get(self.retrieve_book_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIsNotNone(book)


class TestBookGenre(TestCase):
    """
    Test BookGenre urls
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.list_book_genre_path = reverse('book-genre-list')
        self.retrieve_book_genre_path = reverse('book-genre-detail', args=[1])

    def test_get_genres(self):

        response = self.client.get(self.list_book_genre_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_genre(self):
        create_book()

        response = self.client.get(self.retrieve_book_genre_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        genre = BookGenre.objects.get(id=1)
        self.assertIsNotNone(genre)


class TestBookAuthor(TestCase):
    """
    Test BookAuthor urls
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.list_book_author_path = reverse('book-author-list')
        self.retrieve_book_author_path = reverse(
            'book-author-detail', args=[1])

    def test_get_authors(self):

        response = self.client.get(self.list_book_author_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_author(self):
        create_book()

        response = self.client.get(self.retrieve_book_author_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        author = BookAuthor.objects.get(id=1)
        self.assertIsNotNone(author)


class TestBookLanguage(TestCase):
    """
    Test BookLanguage urls
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.list_book_language_path = reverse('book-language-list')
        self.retrieve_book_language_path = reverse(
            'book-language-detail', args=[1])

    def test_get_languages(self):

        response = self.client.get(self.list_book_language_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_language(self):
        create_book()

        response = self.client.get(self.retrieve_book_language_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        language = BookLanguage.objects.get(id=1)
        self.assertIsNotNone(language)
