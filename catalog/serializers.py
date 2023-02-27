from django.http import JsonResponse
from rest_framework import serializers

from catalog.models import Author, Books, Reader


class AuthorViewSetSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False)

    class Meta:
        model = Author
        fields = '__all__'


class ReaderViewSetSerializer(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(many=True, required=False, queryset=Books.objects.all(),
                                                slug_field='name')

    class Meta:
        model = Reader
        fields = '__all__'


class BooksListSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(many=True, read_only=True, slug_field='lastname')

    class Meta:
        model = Books
        fields = '__all__'


class BooksRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    authors = AuthorViewSetSerializer(many=True, read_only=True)

    class Meta:
        model = Books
        fields = '__all__'


class BooksCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    authors = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Author.objects.all(),
        slug_field='lastname'
    )

    class Meta:
        model = Books
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._authors = self.initial_data.pop('authors')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        books = Books.objects.create(**validated_data)
        try:
            for author in self._authors:
                author_obj = Author.objects.get(lastname=author)
                books.authors.add(author_obj)

        except Author.DoesNotExist:
            raise serializers.ValidationError({"error": "Такого автора нет в каталоге, добавьте сначала автора "
                                                        "потом книгу"})
        books.save()
        return books





