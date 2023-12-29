from rest_framework.serializers import ModelSerializer
from base.models import Book, BookAuthor, BookGenre, BookLanguage


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.name
        representation['book_genre'] = instance.book_genre.genre
        representation['language'] = instance.language.language
        return representation


class BookAuthorSerializer(ModelSerializer):

    class Meta:
        model = BookAuthor
        fields = '__all__'


class BookGenreSerializer(ModelSerializer):

    class Meta:
        model = BookGenre
        fields = '__all__'


class BookLanguageSerializer(ModelSerializer):

    class Meta:
        model = BookLanguage
        fields = '__all__'
