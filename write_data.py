import csv
import os
from datetime import datetime
import sqlite3

####################################### 
#
# by. JayHyeon (22/10/31)
# get_now_day = Crawling 시작 시간을 파악 후 해당 시간에 맞춰 category, brand dir 생성
# 아래 함수 호출마다 해당 함수를 호출하게 되면 파일별 디렉토리의 시간이 달라질 수도 있음
# 따라서 전역변수에 Crawling 시작 시간 할당
#######################################
def get_now_day():
    month = datetime.today().month
    day = datetime.today().day
    now_day = f'{month}_{day}'
    return now_day

now_day = get_now_day()

####################################### 
#
# by. JayHyeon (22/1O/25)
# write_goods_total_data = 모든 물품의 상세정보가 담긴 리스트를 csv 파일로 작성하기 위한 함수
# args ->
# wirte.writerows() = List 타입으로 주어지는 인자의 모든 값을 작성하는 함수
#
#######################################
def write_goods_total_data(goods_total_data):
    total_goods_detail_info_list = goods_total_data
    
    dir_path = f'./llatrof/data/{now_day}'
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    f = open(f'{dir_path}/data.csv','w')
    writer = csv.writer(f)
    writer.writerows(total_goods_detail_info_list)
    f.close()

#######################################
#
# by. JayHyeon (22/1O/25)
# write_goods_total_data = 모든 물품의 상세정보가 담긴 리스트를 csv 파일로 작성하기 위한 함수
# args ->
# wirte.writerows() = List 타입으로 주어지는 인자의 모든 값을 작성하는 함수
#
#######################################
def write_category():
    csv_file = open('./llatrof/data.csv','r',encoding='utf-8')
    f = csv.reader(csv_file)

    goods_list = list(f)
    category_set = set()
    for goods in goods_list:
        category = goods[2]
        category_set.add(category)

    category_list = [
        ['id', 'category'],
    ]
    for category_num, category in enumerate(category_set):
        record = [category_num + 1, category]
        category_list.append(record)

    dir_path = f'./llatrof/category/{now_day}'
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    w = open(f'{dir_path}/category.csv','w')
    writer = csv.writer(w)
    writer.writerows(category_list)
    w.close()

def write_brand():
    csv_file = open('./llatrof/data.csv','r',encoding='utf-8')
    f = csv.reader(csv_file)
    
    goods_list = list(f)
    brand_set = set()
    for goods in goods_list:
        brand = goods[3]
        brand_set.add(brand)

    brand_list = [
        ['id', 'brand'],
    ]
    for brand_num, brand in enumerate(brand_set):
        record = [brand_num + 1, brand]
        brand_list.append(record)
    
    dir_path = f'./llatrof/brand/{now_day}'
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    w = open(f'{dir_path}/brand.csv','w')
    writer = csv.writer(w)
    writer.writerows(brand_list)
    w.close()

#######################################
#
# by. JayHyeon (22/11/1)
# import_data = data.csv 를 DB 에 import 하기 위한 함수
# FK Field 에 따라 Field 순서가 임의로 배정됨에 따라
# 이를 해결하기 위해 코드롤 통한 Import Data 과정 필요
# DB 에 record 추가하는 로직으로써 main.py 에 기재 X
#######################################
def import_data():
    csv_file = open('./llatrof/data.csv','r',encoding='utf-8')
    f = csv.reader(csv_file)

    goods_list = list(f)
    db = sqlite3.connect('./llatrof/db.sqlite3')
    cursor = db.cursor()

    table_name = 'articles_article'
    for goods in goods_list:
        goods_url, goods_img_url, goods_category, goods_brand = goods
        fields_value = (goods_url, goods_img_url, goods_brand, goods_category)

        cursor.execute(f'INSERT INTO {table_name} (goods_url, goods_img_url, goods_brand, goods_category) VALUES (?, ?, ?, ?)',
            fields_value
        )
        db.commit()
    db.close()