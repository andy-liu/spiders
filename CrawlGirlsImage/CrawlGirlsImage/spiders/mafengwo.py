# -*- coding: utf-8 -*-
import scrapy
import requests

class MafengwoSpider(scrapy.Spider):
    name = 'mafengwo'
#     allowed_domains = ['http://www.mafengwo.cn/i/6870266.html']
    start_urls = ['http://www.mafengwo.cn/photo/12700/scenery_6870266_1.html']

    def parse(self, response):
        print(response.status)
        selector = scrapy.Selector(response)
        girls = selector.xpath('//dl[@class="adp_style1"]/dt')
        print(len(girls))
#         print(girls)
        i=0
        for each in girls:
            girl_image_url = each.xpath('div[@class="part0"]/a/img/@data-original').extract()[0]
            file_path = 'D:\\spider_result\\image006\\' + 'image' + '_' + str(i) + ".jpg"
            try:
                image= requests.get(girl_image_url, timeout=20)
            except Exception:
                continue
            with open(file_path, 'wb') as fp:
                fp.write(image.content)
                i = i+1
