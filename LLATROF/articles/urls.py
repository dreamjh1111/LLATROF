from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('category/<category>/', views.category_goods, name='category_goods'),
    path('brand/', views.brand, name='brand'),
    path('brand/<brand>/', views.brand_goods, name='category_brand'),
]
