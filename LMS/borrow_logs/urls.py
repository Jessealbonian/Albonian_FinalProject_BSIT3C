from django.urls import path
from .views import BorrowLogListCreateView, BorrowLogDetailView

urlpatterns = [
    path('borrow-logs/', BorrowLogListCreateView.as_view(), name='borrow-log-list-create'),
    path('borrow-logs/<int:pk>/', BorrowLogDetailView.as_view(), name='borrow-log-detail'),
] 