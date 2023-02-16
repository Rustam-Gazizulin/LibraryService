from django.contrib import admin
from .models import Reader, Author, Books

admin.site.register(Reader)
admin.site.register(Author)
admin.site.register(Books)

