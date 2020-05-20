# -*- coding: utf-8 -*-
import scrapy


class ZhihuarticleSpider(scrapy.Spider):
    name = 'ZhiHuArticle'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v3/oauth/sign_in']
    # custom_settings = {
    #     'DEFAULT_REQUEST_HEADERS': {
    #         'User-Agent': UserAgent().random
    #     }
    # }

    def parse(self, response):
        if response.status == 401:
            self.zhihu_login("13419413148", "ZRD887799")
        else:
            print(response.text)

    def zhihu_login(self, user, passwd):
        pass