# -*- coding: utf-8 -*-
import scrapy
import requests

class AutumnwinterSpider(scrapy.Spider):
    name = 'autumnwinter'
#     allowed_domains = ['http://www.vogue.co.uk/shows/autumn-winter-2015-ready-to-wear/westminster-university/collection']
    start_urls = ['http://www.vogue.co.uk/shows/autumn-winter-2015-ready-to-wear/westminster-university/collection']

    def parse(self, response):
        selector = scrapy.Selector(response)
        images = selector.xpath('//ul[@class="global__list-reset a-gallery__image-list "]/li[@class="a-gallery__image-listitem a-gallery__image-listitem--image  js-g-image"]')
        i=0
        for each in images:
            image_url = each.xpath('figure/div[@class="c-figure__container"]/div[@class="c-figure__wrapper"]/img/@data-src').extract()[0]
            print(image_url)
            file_path = 'D:\\spider_result\\image004\\' + 'image' + '_' + str(i) + ".jpg"
            try:
                image= requests.get(image_url, timeout=10)
            except Exception:
                continue
            with open(file_path, 'wb') as fp:
                fp.write(image.content)
            i = i+1

