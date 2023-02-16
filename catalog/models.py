from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=30, verbose_name='Имя автора')
    lastname = models.CharField(max_length=30, verbose_name='Фамилия автора')
    img = models.ImageField(upload_to='image/', blank=True, verbose_name='Фото автора')
    date_of_created = models.DateField(auto_now_add=True, editable=True, verbose_name='Дата создания')
    date_edited = models.DateField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['lastname']

    def __str__(self):
        return self.firstname


class Books(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    number_of_pages = models.PositiveIntegerField(blank=True, verbose_name='Количество страниц', editable=True)
    number_of_books = models.PositiveIntegerField(blank=True, verbose_name='Количество книг', editable=True)
    date_of_created = models.DateField(auto_now_add=True, editable=True, verbose_name='Дата создания')
    date_edited = models.DateField(auto_now=True, verbose_name='Дата редактирования')
    author = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Reader(models.Model):
    firstname = models.CharField(max_length=30, verbose_name='Имя читателя')
    lastname = models.CharField(max_length=30, verbose_name='Фамилия читателя')
    phone = models.BigIntegerField(verbose_name='Номер телефона')
    status_reader = models.BooleanField(default=True)
    active_books = models.ManyToManyField(Books)

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.firstname







