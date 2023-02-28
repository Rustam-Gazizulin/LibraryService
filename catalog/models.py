from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=30, verbose_name='Имя автора')
    lastname = models.CharField(max_length=30, verbose_name='Фамилия автора')
    img = models.ImageField(upload_to='image/', blank=True, verbose_name='Фото автора')
    date_of_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_edited = models.DateField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['lastname']

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Books(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название', unique=True)
    description = models.TextField(max_length=2000, verbose_name='Описание')
    number_of_pages = models.PositiveIntegerField(verbose_name='Количество страниц')
    number_of_books = models.PositiveIntegerField(verbose_name='Количество книг')
    date_of_created = models.DateField(auto_now_add=True, editable=True, verbose_name='Дата создания')
    date_edited = models.DateField(auto_now=True, verbose_name='Дата редактирования')
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Reader(models.Model):
    firstname = models.CharField(max_length=30, verbose_name='Имя читателя')
    lastname = models.CharField(max_length=30, verbose_name='Фамилия читателя')
    phone = models.BigIntegerField(verbose_name='Номер телефона', unique=True)
    status_reader = models.BooleanField(default=True, verbose_name="Статус")
    active_books = models.ManyToManyField(Books, related_name='books', blank=True)

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def display_books(self):
        return ' | '.join([active_books.name for active_books in self.active_books.all()])
    display_books.short_description = 'Книги на руках'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'







