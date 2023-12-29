from django.utils import timezone

from base.models import Book, BookAuthor, BookGenre, BookLanguage


def create_book():
    BookAuthor.objects.create(name='Test Author', surname='Surname')
    BookGenre.objects.create(genre='Test Genre')
    BookLanguage.objects.create(language='English')
    Book.objects.create(title='Test Book',
                        author=BookAuthor.objects.get(id=1),
                        description='Test',
                        book_genre=BookGenre.objects.get(id=1),
                        language=BookLanguage.objects.get(id=1),
                        book_created_at=timezone.make_aware(
                            timezone.datetime(2000, 1, 1, 12, 0, 0)),
                        page_count=100)
    return Book.objects.get(id=1)
