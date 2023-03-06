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

    def validate(self, attrs):
        if len(attrs['active_books']) > 3:
            raise serializers.ValidationError('Нельзя выдавать больше 3 книг в 1 руки')
        return attrs

    def create(self, validated_data):
        books_data = validated_data.pop('active_books')
        reader = Reader.objects.create(**validated_data)
        for book_data in books_data:
            book = Books.objects.get(pk=book_data.id)
            if book.number_of_books > 0:
                book.number_of_books -= 1
                book.save()
                reader.active_books.add(book)
            else:
                raise serializers.ValidationError(f"Книги {book.name} нет в наличии")
        return reader

    def update(self, instance, validated_data):
        if validated_data['active_books']:
            for book in validated_data['active_books']:
                if book not in instance.active_books.all():
                    if book.number_of_books > 0:
                        book.number_of_books -= 1
                        book.save()
                    else:
                        raise serializers.ValidationError('Книги нет в наличии')
            for book in instance.active_books.all():
                if book not in validated_data['active_books']:
                    book.number_of_books += 1
                    book.save()
            return super().update(instance, validated_data)
        else:
            return super().update(instance, validated_data)




class BookViewSetSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='lastname')

    number_of_pages = serializers.IntegerField(validators=[NumbersPageValidator()])

    class Meta:
        model = Books
        fields = '__all__'







