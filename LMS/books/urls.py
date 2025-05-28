from django.urls import path, include
from books.views import (
    CategoryListCreateView,
    CategoryDetailView,
    booksListCreateView,
    booksDetailView,
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('books/', booksListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', booksDetailView.as_view(), name='book-detail'),
]