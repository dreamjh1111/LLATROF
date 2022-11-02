import crawling
import write_data

# main 실행부
goods_total_url_list = crawling.get_goods_total_url_list()

goods_total_detail_info_list = crawling.get_total_goods_detail_info(goods_total_url_list)

write_data.write_goods_total_data(goods_total_detail_info_list)

write_data.write_category()

write_data.write_brand()