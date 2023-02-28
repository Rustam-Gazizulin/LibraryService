from rest_framework.viewsets import ModelViewSet

from catalog.models import Author, Books, Reader
from catalog.serializers import AuthorViewSetSerializer, ReaderViewSetSerializer, BookViewSetSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorViewSetSerializer


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderViewSetSerializer


class BookViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookViewSetSerializer


