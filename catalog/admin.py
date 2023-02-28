from django.contrib import admin
from django.db.models import QuerySet
from django.utils.html import format_html
from django.urls import reverse

from .models import Reader, Author, Books


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'number_of_books', 'authors_link')
    search_fields = ('name',)
    actions = ['zero_nums_books']

    def authors_link(self, obj):
        author = obj.authors
        url = reverse("admin:catalog_author_changelist") + str(author.pk)
        return format_html(f'<a href="{url}"> {author} </a>')

    authors_link.short_description = 'Авторы'

    @admin.action(description='Нет в наличии')
    def zero_nums_books(self, request, queryset: QuerySet):
        queryset.update(number_of_books=0)
        self.message_user(request, f'Книг нет в наличии')


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'phone', 'status_reader', 'display_books')
    list_filter = ('status_reader',)
    actions = ['change_status_reader']

    @admin.action(description='Изменить статус читателя')
    def change_status_reader(self, request, queryset: QuerySet):
        count = queryset.update(status_reader=False)
        self.message_user(request, f'Заблокировано {count} читателей')

    # @admin.action(description='Удалить книги у читателя')
    # def zero_active_books(self, request, queryset: QuerySet):
    #     books = Books.objects.all()
    #     for book in books:
    #         queryset.delete(Reader.active_books[book])
    #     self.message_user(request, f'У читателей нет книг')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'date_of_created')


admin.site.register(Reader, ReaderAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Books, BookAdmin)

