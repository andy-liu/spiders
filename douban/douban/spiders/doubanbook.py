# -*- coding: utf-8 -*-
import scrapy
import re
from douban.items import DoubanItem
from audioop import ratecv

class DoubanbookSpider(scrapy.Spider):
    name = 'doubanbook'
#     allowed_domains = ['www.douban.com/doulist/1264675/']
    start_urls = ['https://www.douban.com/doulist/1264675//']

    def parse(self, response):
#         print ('test')
#         print (response.body)
        item = DoubanItem()
        selector = scrapy.Selector(response)
        books = selector.xpath('//div[@class="bd doulist-subject"]')
        for each in books:
            title = each.xpath('div[@class="title"]/a/text()').extract()[0]
            rate = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            author = re.search('<div class="abstract">(.*?)<br',each.extract(),re.S).group(1)
            title = title.replace(' ','').replace('\n','')
            author = author.replace(' ','').replace('\n','')
            item['title'] = title
            item['rate'] = rate
            item['author'] = author
            yield item
            next_page = selector.xpath('//span[@class="next"]/link/@href').extract()
            if next_page:
                next = next_page[0]
                yield scrapy.http.Request(next,callback=self.parse)






