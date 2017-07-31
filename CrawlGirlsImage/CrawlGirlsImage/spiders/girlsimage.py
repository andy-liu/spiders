# -*- coding: utf-8 -*-
import scrapy
import requests

class GirlsimageSpider(scrapy.Spider):
    name = 'girlsimage'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-0.html/']

    def parse(self, response):
        base_url = 'http://www.xiaohuar.com'
        print(response.status)
        selector = scrapy.Selector(response)
        girls = selector.xpath('//div[@class="item_list infinite_scroll"]/div[@class="item masonry_brick"]')
        for each in girls:
            girl_image_url = each.xpath('div[@class="item_t"]/div[@class="img"]/a/img/@src').extract()[0]
#             name = each.xpath('div[@class="item_t"]/div[@class="img"]/span/text()').extract()[0]
            school = each.xpath('div[@class="item_t"]/div[@class="title"]/span/a/text()').extract()[0]
            absolute_image_url = base_url + girl_image_url
            file_path = 'D:\\spider_result\\image002\\' + 'image' + '_' + school + ".jpg"
            image= requests.get(absolute_image_url, timeout=10)
            with open(file_path, 'wb') as fp:
                fp.write(image.content)
            
        all_urls = selector.xpath('//a/@href').extract()#提取界面所有的url
        for url in all_urls:#遍历获得的url，如果满足条件，继续爬取
            if url.startswith('http://www.xiaohuar.com/list-1-'):
                yield scrapy.http.Request(url, callback=self.parse)
