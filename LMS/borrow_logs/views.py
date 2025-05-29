from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import borrow_logs
from .serializers import borrow_logsSerializer
from django.utils import timezone
from LMS.decorators import rate_limit

class BorrowLogListCreateView(generics.ListCreateAPIView):
    queryset = borrow_logs.objects.all()
    serializer_class = borrow_logsSerializer
    permission_classes = [IsAuthenticated]

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = borrow_logs.objects.all()
        # Filter by borrower if provided
        borrower = self.request.query_params.get('borrower', None)
        if borrower:
            queryset = queryset.filter(borrower_name=borrower)
        # Filter by return status if provided
        is_returned = self.request.query_params.get('is_returned', None)
        if is_returned is not None:
            queryset = queryset.filter(is_returned=is_returned.lower() == 'true')
        return queryset


class BorrowLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = borrow_logs.objects.all()
    serializer_class = borrow_logsSerializer
    permission_classes = [IsAuthenticated]
    from LMS.decorators import rate_limit

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

    def perform_update(self, serializer):
        # If marking as returned, set the return date
        if 'is_returned' in self.request.data and self.request.data['is_returned']:
            serializer.save(date_returned=timezone.now())
        else:
            serializer.save()