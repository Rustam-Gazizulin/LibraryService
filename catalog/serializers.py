from rest_framework import serializers

from catalog.models import Author, Books, Reader
from catalog.validators import PhoneValidator, NumbersPageValidator


class AuthorViewSetSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False)

    class Meta:
        model = Author
        fields = '__all__'


class ReaderViewSetSerializer(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(many=True, required=False, queryset=Books.objects.all(),
                                                slug_field='name')

    phone = serializers.CharField(validators=[PhoneValidator()])

    class Meta:
        model = Reader
        fields = '__all__'


class BookViewSetSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(many=True, required=False, queryset=Author.objects.all(),
                                           slug_field='lastname')

    number_of_pages = serializers.IntegerField(validators=[NumbersPageValidator()])

    class Meta:
        model = Books
        fields = '__all__'







