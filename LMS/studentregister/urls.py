from django.urls import path
from .views import StudentRegListCreateView, StudentRegRetrieveUpdateDestroyView
    
urlpatterns = [
    path('', StudentRegListCreateView.as_view(), name='StudentReg_list_create'),
    path('<int:pk>/', StudentRegRetrieveUpdateDestroyView.as_view(), name='StudentReg_detail'),
]