from django.contrib import admin

from base.models import BookAuthor, Book, BookGenre, BookLanguage


admin.site.register([BookAuthor, Book, BookGenre, BookLanguage])
