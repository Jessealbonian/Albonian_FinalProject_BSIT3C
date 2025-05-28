from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Category, books
from .serializers import CategorySerializer, booksSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class booksListCreateView(generics.ListCreateAPIView):
    queryset = books.objects.all()
    serializer_class = booksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = books.objects.all()
        # Filter by category if provided
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__name=category)
        
        # Filter by status if provided
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        
        # Filter by author if provided
        author = self.request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(author__icontains=author)
        
        # Filter by title if provided
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        
        return queryset


class booksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = books.objects.all()
    serializer_class = booksSerializer
    permission_classes = [IsAuthenticated]
# Create your views here.
