import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/heyon/Desktop/JAY/LLATROF/chromedriver")
URL = 'https://www.musinsa.com/categories/item/003?d_cat_cd=003&brand=&list_kind=small&sort=pop_category&sub_sort=&page=1&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=measure_5%5E110%5E120'
driver.get(URL)

