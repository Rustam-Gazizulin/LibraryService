from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from catalog.models import Author, Books, Reader
from catalog.serializers import AuthorViewSetSerializer, BooksListSerializer, \
    BooksCreateSerializer, BooksRetrieveUpdateDestroySerializer, ReaderViewSetSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorViewSetSerializer


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderViewSetSerializer


class BooksListView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksListSerializer


class BooksRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksRetrieveUpdateDestroySerializer


class BooksCreateView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksCreateSerializer
