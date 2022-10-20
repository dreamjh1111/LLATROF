import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Hide Chrome
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# driver = webdriver.Chrome("/Users/heyon/Desktop/JAY/LLATROF/chromedriver", chrome_options=options)

driver = webdriver.Chrome("/Users/heyon/Desktop/JAY/LLATROF/chromedriver")
URL = 'https://www.musinsa.com/categories/item/003?d_cat_cd=003&brand=&list_kind=small&sort=pop_category&sub_sort=&page=1&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=measure_5%5E110%5E120'
driver.get(URL)
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[12]/button[2]').click()

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

def get_goods_url(goods):
    get_goods_url = goods.find_element(By.CSS_SELECTOR, f'div.li_inner > div.list_img > a')
    goods_url = get_goods_url.get_attribute('href')
    return goods_url

def get_goods_img_url(goods):
    get_goods_img_url = goods.find_element(By.CSS_SELECTOR, f'div.li_inner > div.list_img > a > img')
    goods_img_url = get_goods_img_url.get_attribute('src')
    return goods_img_url

def get_goods_data():
    goods_data_lst = [
        ['id', 'goods_url', 'goods_img_url'],
    ]
    goods_num = 1
    for goods in get_goods_list():
        goods_url = get_goods_url(goods)
        goods_img_url = get_goods_img_url(goods)
        goods_data = [goods_num, goods_url, goods_img_url]
        goods_data_lst.append(goods_data)
        goods_num += 1
    return goods_data_lst

def get_total_page_counts():
    page_counts = driver.find_element(By.CLASS_NAME, 'totalPagingNum').text
    return int(page_counts)

def write_data_from_bottom():
    scroll_to_bottom()
    f = open('data.csv', 'w')
    writer = csv.writer(f)
    writer.writerows(get_goods_data())
    f.close()