import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/heyon/Desktop/JAY/LLATROF/chromedriver")
URL = 'https://www.musinsa.com/categories/item/003?d_cat_cd=003&brand=&list_kind=small&sort=pop_category&sub_sort=&page=1&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=measure_5%5E110%5E120'
driver.get(URL)

def scroll_to_bottom():
    before_location = driver.execute_script("return window.pageYOffset")
    while True:
        # 현재 위치 + 100으로 스크롤 이동   
        driver.execute_script(f"window.scrollTo(0,{before_location + 100})")
        time.sleep(0.05)
        after_location = driver.execute_script("return window.pageYOffset")
        # 더 이상 스크롤이 늘어나지 않으면 종료
        if before_location == after_location:
            break
        else:
            before_location = driver.execute_script("return window.pageYOffset")

def get_goods_list():
    goods_location = driver.find_elements(By.CSS_SELECTOR, '#goods_list > div.boxed-list-wrapper > div.list-box.box > #searchList > li')
    return goods_location