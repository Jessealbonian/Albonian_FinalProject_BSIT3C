from rest_framework import generics, permissions
from .models import StudentReg
from .serializers import StudentRegSerializer
from LMS.decorators import rate_limit

class StudentRegListCreateView(generics.ListCreateAPIView):
    serializer_class = StudentRegSerializer
    permission_classes = [permissions.IsAuthenticated]

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return StudentReg.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentRegRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentRegSerializer
    permission_classes = [permissions.IsAuthenticated]

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return StudentReg.objects.filter(user=self.request.user)