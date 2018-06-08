# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import MovieprojectItem

from scrapy_redis.spiders import RedisCrawlSpider

class FilmSpider(RedisCrawlSpider):
    name = 'film'
    allowed_domains = ['www.dy2018.com']
    # start_urls = ['https://www.dy2018.com/0/']
    redis_key = 'start_urls'
    # https://www.dy2018.com/0/index_2.html
    # https://www.dy2018.com/3/
    rules = (
        Rule(LinkExtractor(allow=r'/\d+/index_\d+\.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tables = response.xpath('//table[@class="tbspan"]')

        for t in tables:
            item = MovieprojectItem()
            #     获取电影名
            #     获取介绍
            title = t.xpath('.//tr[2]//a[2]/text()').extract()[0]
            info = ''.join(t.xpath('.//tr[4]//p/text()').extract())

            info = info.replace('\u3000', '')
            item['title'] = title
            item['info'] = info
            yield item