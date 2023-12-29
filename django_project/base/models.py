from django.db import models


class BookAuthor(models.Model):
    name = models.CharField('Ім’я', max_length=255, blank=False, null=False)
    pen_name = models.CharField('Псевдонім',
                                max_length=255,
                                blank=True,
                                null=True)
    surname = models.CharField('Прізвище',
                               max_length=255,
                               blank=True,
                               null=True)
    birthday_date = models.DateField('Дата народження',
                                     blank=True,
                                     null=True)

    def __str__(self):
        return f'ID: {self.id} | Name: {self.name} {self.surname}'

    class Meta:
        verbose_name = 'Автор книги'
        verbose_name_plural = 'Автори книги'


class BookGenre(models.Model):
    genre = models.CharField('Жанр',
                             max_length=255,
                             blank=False,
                             null=False)
    description = models.TextField('Опис', blank=True, null=True)

    def __str__(self):
        return f'ID: {self.id} | Name: {self.genre}'

    class Meta:
        verbose_name = 'Жанр книги'
        verbose_name_plural = 'Жанри книг'


class BookLanguage(models.Model):
    language = models.CharField('Мова',
                                max_length=255,
                                blank=False,
                                null=False)

    def __str__(self):
        return f'ID: {self.id} | Name: {self.language}'

    class Meta:
        verbose_name = 'Мова'
        verbose_name_plural = 'Мови'


class Book(models.Model):
    title = models.CharField('Назва', max_length=255, blank=False, null=False)
    author = models.ForeignKey(BookAuthor,
                               blank=False,
                               null=True,
                               verbose_name='Автор',
                               on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)
    book_genre = models.ForeignKey(BookGenre,
                                   verbose_name='Жанр книги',
                                   blank=False,
                                   null=True,
                                   on_delete=models.SET_NULL)
    page_count = models.PositiveIntegerField('Кількість сторінок',
                                             blank=False,
                                             null=False)
    language = models.ForeignKey(BookLanguage,
                                 verbose_name='Мова',
                                 max_length=128,
                                 blank=False,
                                 null=True,
                                 on_delete=models.SET_NULL)
    book_created_at = models.DateField('Дата написання книги')

    def __str__(self):
        return f'ID: {self.id} | Name: {self.title}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
