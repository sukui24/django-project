from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from base.tests.fixture import create_book
from base.models import BookGenre, BookAuthor, BookLanguage, Book


class TestBook(TestCase):
    """
    Test Book update and delete operations
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.retrieve_book_path = reverse('book-detail', args=[1])

    def test_delete_book(self):
        book = create_book()
        self.assertIsNotNone(book)
        self.assertEqual(str(book), 'ID: 1 | Name: Test Book')

        response = self.client.delete(self.retrieve_book_path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response_after_delete = self.client.get(self.retrieve_book_path)
        self.assertEqual(str(response_after_delete), '<Response status_code=404, "application/json">')  # NOQA

    def test_update_book(self):
        book = create_book()
        self.assertIsNotNone(book)
        self.assertEqual(str(book), 'ID: 1 | Name: Test Book')

        response = self.client.patch(self.retrieve_book_path, {
            'title': 'updated title'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(id=1)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, 'updated title')


class TestBookGenre(TestCase):
    """
    Test BookGenre urls
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.retrieve_book_genre_path = reverse('book-genre-detail', args=[1])

    def test_delete_genre(self):
        create_book()
        genre = BookGenre.objects.get(id=1)
        self.assertIsNotNone(genre)
        self.assertEqual(str(genre), 'ID: 1 | Name: Test Genre')

        response = self.client.delete(self.retrieve_book_genre_path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response_after_delete = self.client.get(self.retrieve_book_genre_path)
        self.assertEqual(str(response_after_delete), '<Response status_code=404, "application/json">')  # NOQA

    def test_update_genre(self):
        create_book()
        genre = BookGenre.objects.get(id=1)
        self.assertIsNotNone(genre)
        self.assertEqual(str(genre), 'ID: 1 | Name: Test Genre')

        response = self.client.patch(self.retrieve_book_genre_path, {
            'genre': 'updated genre'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_genre = BookGenre.objects.get(id=1)
        self.assertIsNotNone(updated_genre)
        self.assertEqual(updated_genre.genre, 'updated genre')


class TestBookAuthor(TestCase):
    """
    Test BookAuthor urls
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.retrieve_book_author_path = reverse(
            'book-author-detail', args=[1])

    def test_delete_author(self):
        create_book()
        author = BookAuthor.objects.get(id=1)
        self.assertIsNotNone(author)
        self.assertEqual(str(author), 'ID: 1 | Name: Test Author Surname')

        response = self.client.delete(self.retrieve_book_author_path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response_after_delete = self.client.get(self.retrieve_book_author_path)
        self.assertEqual(str(response_after_delete), '<Response status_code=404, "application/json">')  # NOQA

    def test_update_author(self):
        create_book()
        author = BookAuthor.objects.get(id=1)
        self.assertIsNotNone(author)
        self.assertEqual(str(author), 'ID: 1 | Name: Test Author Surname')

        response = self.client.patch(self.retrieve_book_author_path, {
            'name': 'updated author',
            'surname': 'updated surname'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_author = BookAuthor.objects.get(id=1)
        self.assertIsNotNone(updated_author)
        self.assertEqual(updated_author.name, 'updated author')
        self.assertEqual(updated_author.surname, 'updated surname')


class TestBookLanguage(TestCase):
    """
    Test BookLanguage urls
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.retrieve_book_language_path = reverse(
            'book-language-detail', args=[1])

    def test_get_languages(self):
        create_book()
        language = BookLanguage.objects.get(id=1)
        self.assertIsNotNone(language)
        self.assertEqual(str(language), 'ID: 1 | Name: English')

        response = self.client.delete(self.retrieve_book_language_path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response_after_delete = self.client.get(
            self.retrieve_book_language_path)
        self.assertEqual(str(response_after_delete), '<Response status_code=404, "application/json">')  # NOQA

    def test_retrieve_language(self):
        create_book()
        language = BookLanguage.objects.get(id=1)
        self.assertIsNotNone(language)
        self.assertEqual(str(language), 'ID: 1 | Name: English')

        response = self.client.patch(self.retrieve_book_language_path, {
            'language': 'Ukranian'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_language = BookLanguage.objects.get(id=1)
        self.assertIsNotNone(updated_language)
        self.assertEqual(updated_language.language, 'Ukranian')
