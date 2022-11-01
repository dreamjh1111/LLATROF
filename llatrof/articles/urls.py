from django.urls import path
from . import views

url_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]
