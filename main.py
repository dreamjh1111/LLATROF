import crawling

# main 실행부
goods_total_url_list = crawling.get_total_goods_url_list()

goods_total_detail_info_list = crawling.get_total_goods_detail_info(goods_total_url_list)

crawling.write_goods_total_data(goods_total_detail_info_list)