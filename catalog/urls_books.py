from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.BooksListView.as_view()),
    path("<int:pk>/", views.BooksRetrieveView.as_view()),
    path("create/", views.BooksCreateView.as_view()),

    ]
