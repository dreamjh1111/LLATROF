from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

#######################################
#
# by. JaeHyeon (22/1O/26)
# category = goods_category 를 분류하기 위한 함수
# args ->
# categorise = Article Table 내 goods_category Field 를 중복 제거한 QuerySetList
# category_list = goods_category 만 분류한 List
#
#######################################
def category(request):
    categorise = Article.objects.values('goods_category').distinct()

    category_list = []
    for category in categorise:
        category = category['goods_category']
        category_list.append(category)

    context = {
        'category_list': category_list,
    }
    
    return render(request, 'articles/category.html', context)

#######################################
#
# by. JaeHyeon (22/1O/26)
# category_goods = category 기준으로 분류된 goods 만 rendering 하는 함수
# args ->
# goods_list = Article Table 내 goods_category 기준으로 variable routing 을 통해 받은 category(:str) 를 filtering 한 QuerySetList
#
#######################################
def category_goods(request, category):
    goods_list = Article.objects.all().filter(goods_category=category)
    
    context = {
        'goods_list': goods_list,
    }
    return render(request, 'articles/category.html', context)

#######################################
#
# by. JaeHyeon (22/1O/26)
# brand = goods_brand 를 분류하기 위한 함수
# args ->
# brands = Article Table 내 goods_brand Friled 를 중복 제거한 QuerySetList
# brands_list = goods_brand 만 분류한 List
#
#######################################
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

#######################################
#
# by. JaeHyeon (22/1O/26)
# brand_goods = brand 기준으로 분류된 goods 만 rendering 하는 함수
# args ->
# goods_list = Article Table 내 goods_brand 기준으로 variable routing 을 통해 받은 brand(:str) 를 filtering 한 QuerySetList
#
#######################################
def brand_goods(request, brand):
    goods_list = Article.objects.all().filter(goods_brand=brand)
    
    context = {
        'goods_list': goods_list,
    }
    return render(request, 'articles/brand.html', context)