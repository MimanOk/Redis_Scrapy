# -*- coding: utf-8 -*-
# : Time    : 2020/05/19
__author__ = "Miman"

from scrapy_redis.spiders import RedisSpider
from ..items import MeiTuItem
from scrapy import Request
import os
import logging


class MeiTuSpider(RedisSpider):
    name = "meitu"
    allowed_domains = ["www.521609.com"]
    redis_key = "meitu:start_urls"

    # def __init__(self, log_path, store_path=None):
    #     # 判断路径是否存在
    #     if store_path:
    #         if not os.path.exists(store_path):
    #             os.mkdir(store_path)
    #             self.store_path = store_path
    #     if not os.path.exists('//'.join(log_path.split('//')[:-1])):
    #         os.mkdir('//'.join(log_path.split('//')[:-1]))

    # # 设置日志
    # self.logger = logging.getLogger(__name__)
    # self.logger.setLevel(logging.INFO)
    #
    # # log to console
    # log_con = logging.StreamHandler()
    # log_con.setLevel(logging.DEBUG)
    # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)-8s - %(message)s")
    # log_con.setFormatter(formatter)
    # self.logger.addHandler(log_con)
    #
    # # log to file
    # log_file = logging.FileHandler(log_path)
    # log_file.setLevel(logging.WARNING)
    # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)-8s - %(message)s")
    # log_file.setFormatter(formatter)
    # self.logger.addHandler(log_file)

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     settings = crawler.settings
    #     return cls(
    #         store_path=settings.get("MEITU_IMAGE_STORE_PATH", None),
    #         log_path=settings.get("MEITU_LOG_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "meitu.log"))
    #     )

    def log_out(self, e, response):
        print("in file %s" % __file__)
        print("%(error)s from url --> %(url)s" % {"error": e, "url": response.url})

    def parse(self, response):
        print("当前组图 ->> ", response.meta.get("group", None))
        item = MeiTuItem()
        image_list = response.css(".index_img ul li")
        for image in image_list:
            try:
                image_url = "http://" + self.allowed_domains[0] + image.css("a:nth-child(1) img::attr(src)").extract()[0]
                image_desc = image.css("a:nth-child(1) img::attr(alt)").extract()[0].strip()
                for field in item.fields:
                    item[field] = eval(field)
                yield item
            except IndexError as e:
                self.log_out(e, response)
        try:
            base_url = response.css(".listpage li a:contains('下一页')::attr(href)").extract()[0]
            if response.url.endswith('/'):
                next_url = response.url + base_url
            elif response.url.endswith("com"):
                next_url = response.url + '/' + base_url
            else:
                next_url = response.urljoin(base_url)
            group = response.css("li.current a span::text").extract()[0].strip()
        except IndexError as e:
            self.log_out(e, response)
            # 没有下一页，寻找下一组图
            base_url = '/'.join(response.url.split('/')[:-1])
            try:
                body_url = base_url + response.css("li.current + li a::attr(href)").extract()[0]
            except IndexError as e:
                self.log_out(e, response)
                print("spider finished !")
                return
            next_url = base_url + body_url
            group = response.css("li.current + li a span::text").extract()[0].strip()
            print("下一组图 ->> ", group)

        yield Request(url=next_url, meta={'group': group}, callback=self.parse, dont_filter=True)
