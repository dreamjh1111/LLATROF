from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Hide Chrome Options
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# driver = webdriver.Chrome("./chromedriver", chrome_options=options)

#######################################
#
# by. JayHyeon (22/1O/25)
#
# args ->
# driver = Chrome Driver 를 이용해 프로그램 구동
# URL = driver 가 최초로 이동하는 url
# driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[12]/button[2]').click() = 무신사 홈페이지의 남성 카테고리 Selector
#######################################
driver = webdriver.Chrome('./chromedriver')
URL = 'https://www.musinsa.com/categories/item/003?d_cat_cd=003&brand=&list_kind=small&sort=pop_category&sub_sort=&page=1&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=measure_5%5E110%5E120'
driver.get(URL)
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[12]/button[2]').click()

def get_goods_list():
    goods_location = driver.find_elements(By.CSS_SELECTOR, '#goods_list > div.boxed-list-wrapper > div.list-box.box > #searchList > li')
    return goods_location

def get_goods_url(goods):
    get_goods_url = goods.find_element(By.CSS_SELECTOR, f'div.li_inner > div.list_img > a')
    goods_url = get_goods_url.get_attribute('href')
    return goods_url

def get_goods_img_url():
    get_goods_img_url = driver.find_element(By.CSS_SELECTOR, '#detail_bigimg > .product-img > img')
    goods_img_url = get_goods_img_url.get_attribute('src')
    return goods_img_url

def get_total_page_counts():
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'totalPagingNum')))
    page_counts = driver.find_element(By.CLASS_NAME, 'totalPagingNum').text
    return int(page_counts)

def get_goods_url_list():
    goods_url_list = []
    for goods in get_goods_list():
        goods_url = get_goods_url(goods)
        goods_url_list.append(goods_url)
    return goods_url_list

#######################################
#
# by. JaeHyeon (22/10/27)
# get_goods_category = goods detail - category 를 반환하는 함수
# args ->
# goods_category = 해당 goods 의 category 를 나타내는 변수
# '/' 로 분기한 이유는, 트레이닝/조거 같은 경우 동일한 goods 에 트레이닝, 조거
# 구분 지은 후 트레이닝만 category 분류해야함
#######################################
def get_goods_category():
    get_goods_category = driver.find_elements(By.CSS_SELECTOR, '.section_product_summary > div.product_info > p > a')        
    goods_category = get_goods_category[1].text.split(' ')[0]
    if '/' in goods_category:
        goods_category = goods_category.split('/')
        return goods_category[0]
    return goods_category

def get_goods_brand():
    get_goods_brand = driver.find_elements(By.CSS_SELECTOR, '.section_product_summary > div.product_info > p > a')        
    temp_goods_brand = get_goods_brand[2].text
    goods_brand = temp_goods_brand[1:len(temp_goods_brand)-1]
    return goods_brand

def get_page_url(page):
    url = f'https://www.musinsa.com/categories/item/003?d_cat_cd=003&brand=&list_kind=small&sort=pop_category&sub_sort=&page={page}&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=measure_5%5E110%5E120'
    return url

def get_to_next_page(url):
    driver.get(url)

#######################################
#
# by. JayHyeon (22/1O/25)
# get_goods_total_url_list = 전체 물품의 url 을 List 에 담아 반환하는 함수
# args ->
# total_goods_url_list = 현재 페이지의 물품 url 을 담은 List
# get_to_next_page() = 인자의 값(다음 페이지)으로 driver 가 이동
#
#######################################
def get_goods_total_url_list():
    total_goods_url_list = []
    for page in range(2, get_total_page_counts()):
        total_goods_url_list += get_goods_url_list()
        
        next_page_url = get_page_url(page)
        get_to_next_page(next_page_url)
    return total_goods_url_list

#######################################
#
# by. JayHyeon (22/1O/25)
# get_total_goods_detail_info = 모든 물품의 url 이 담긴 List 를 순회하면서 물품 별 상세 정보를 반환하기 위한 함수
# args ->
# driver.get(goods_url) = 해당 url 로 chrome driver 가 이동
# temp_goods_detail_info = 상품별 info 를 2차원 배열(total_goods_detail_info_list) 에 담기위한 임시 List
#
#######################################
def get_total_goods_detail_info(goods_total_url_list):
    goods_detail_info_list = []
    for goods_url in goods_total_url_list:
        driver.get(goods_url)

        goods_img_url = get_goods_img_url()
        goods_category = get_goods_category()
        goods_brand = get_goods_brand()
        
        temp_goods_detail_info = [goods_url, goods_img_url, goods_category, goods_brand]
        goods_detail_info_list.append(temp_goods_detail_info)
    return goods_detail_info_list