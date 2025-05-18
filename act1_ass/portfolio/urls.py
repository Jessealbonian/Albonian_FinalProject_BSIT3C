from django.urls import path
from .views import index
from .views import dshbrd
from .views import portfolio

app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index/'),
    
    path('dshbrd/home/', dshbrd, name='dshbrd/home/'),
    path('dshbrd/report/', dshbrd, name='dshbrd/report/'),
    path('dshbrd/settings/', dshbrd, name='/dshbrd/settings/'),

    path('portfolio/', portfolio, name='portfolio'),
    path('dshbrd/home/', dshbrd, name='dshbrd/'),
]
