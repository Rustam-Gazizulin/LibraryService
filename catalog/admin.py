from django.contrib import admin
from .models import Reader, Author, Books


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Reader)
admin.site.register(Author)
admin.site.register(Books, BookAdmin)

