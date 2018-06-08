# -*- coding: utf-8 -*-
import scrapy

from ..items import MovieprojectItem
# 先使用scrapy

# 然后使用scrapy_redis

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.dy2018.com']

    # 剧情的列表
    start_urls = ['https://www.dy2018.com/0/']

    def parse(self, response):

        tables = response.xpath('//table[@class="tbspan"]')


        for t in tables:
            item = MovieprojectItem()
        #     获取电影名
        #     获取介绍
            title = t.xpath('.//tr[2]//a[2]/text()').extract()[0]
            info = ''.join(t.xpath('.//tr[4]//p/text()').extract())

            info = info.replace('\u3000','')
            item['title'] = title
            item['info'] = info
            yield item

