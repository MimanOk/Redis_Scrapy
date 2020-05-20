# -*- coding: utf-8 -*-

from user_agent import generate_user_agent
from scrapy import Spider, Request
from ..items import UserItem
import json

class ZhiHuUserSpider(Spider):
    name = 'ZhiHuUserSpider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']
    # custom_settings = {
    #     'DEFAULT_REQUEST_HEADERS': {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #         'Accept-Language': 'en',
    #         'User-Agent': generate_user_agent()
    #     }
    # }
    user_url = "https://www.zhihu.com/people/{url_token}"
    follower_include = "data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics"
    follower_url = "https://www.zhihu.com/api/v4/members/{url_token}/followees?include={include}&offset={offset}&limit={limit}"


    def start_requests(self):
        follower_start_url = self.follower_url.format(url_token="li-ming-ze-52-87", include=self.follower_include, offset=0, limit=20)
        user_start_url = self.user_url.format(url_token="li-ming-ze-52-87")
        yield Request(follower_start_url, callback=self.followerParse)
        yield Request(user_start_url, callback=self.userParse)

    def followerParse(self, response):
        res = json.loads(response.text)
        for user in res['data']:
            yield Request(self.user_url.format(url_token=user['url_token']), meta={'url_token': user['url_token']}, callback=self.userParse)
            # print("Out----->>", user)
        if not res['paging']['is_end']:
            next_url = res['paging']['next']
            yield Request(next_url, callback=self.followerParse)


    def userParse(self, response):
        url_token = response.meta['url_token']
        items = UserItem()
        selectors = json.loads(response.xpath('//script[@id="js-initialData"]/text()').extract()[0])
        users = selectors['initialState']['entities']['users']
        items['name'] = users[url_token]['name']
        items['headline'] = users[url_token]['headline']
        items['gender'] = users[url_token]['gender']
        items['description'] = users[url_token]['description']
        items['business'] = users[url_token]['business']['name']
        if users[url_token]['locations']:
            items['locations'] = users[url_token]['locations'][0]['name']
        else:
            items['locations'] = ''
        yield items
