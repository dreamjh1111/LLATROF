from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def category(request):
    categorise = Article.objects.values('goods_category').distinct()

    category_list = []
    for category in categorise:
        category = category['goods_category']
        category_list.append(category)

    context = {
        'cetegories': category_list,
    }
    
    return render(request, 'articles/category.html', context)


def category_goods(request, category):
    goods_list = Article.objects.all().filter(goods_category=category)
    
    context = {
        'goods_list': goods_list,
    }
    return render(request, 'articles/category.html', context)

def brand(request):
    brands = Article.objects.values('goods_brand').distinct()
    brands_list = []
    for brand in brands:
        brand = brand['goods_brand']
        brands_list.append(brand)
    context = {
        'brands_list': brands_list,
    }
    
    return render(request, 'articles/brand.html', context)

def brand_goods(request, brand):
    goods_list = Article.objects.all().filter(goods_brand=brand)
    
    context = {
        'goods_list': goods_list,
    }
    print(goods_list)
    return render(request, 'articles/brand.html', context)