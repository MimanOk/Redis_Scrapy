# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import redis
import random
from fake_useragent import UserAgent


class SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DownloadMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self, settings):
        host = settings.get("REDIS_HOST", "127.0.0.1")
        port = settings.get("REDIS_PORT", 6379)
        db = settings.get("REDIS_DB", 0)
        start_url = settings.get("MEITU_START_URL", None)
        try:
            self.re_db = redis.Redis(host=host, port=port, db=db)
        except BaseException as e:
            print("链接库失败： %s", e)
        if start_url:
            self.re_db.lpush("meitu:start_urls", start_url)
        print("-" * 15, " ip池加载完成 ", "-" * 15)

        self.ua = UserAgent()
        self.ua_type = settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(crawler.settings)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    @property
    def get_ip(self):
        ip = self.re_db.blpop("proxies", 10)[1]
        if not ip:
            print("\033[0;33mip pool is empty !\033[0m")
            return random.choice(["http://177.92.67.230:53281", "http://218.204.153.156:8080", "http://82.137.244.151:8080", "http://113.121.22.201:9999", "http://103.143.20.78:8080", "http://171.35.171.105:9999"])
        if isinstance(ip, bytes):
            return "http://" + ip.decode("utf-8")
        return "http://" + ip

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.headers.setdefault("User-Agent", getattr(self.ua, self.ua_type))
        proxy = self.get_ip
        request.meta['proxy'] = proxy
        request.meta['dont_redirect'] = True
        # request.meta['handle_httpstatus_list'] = [302]
        request.meta['download_timeout'] = 15
        print("-" * 10, "设置代理: ", proxy, "-" * 10)
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        if response.status >= 200 and response.status <= 401:
            proxy = request.meta.get("proxy", None)
            if proxy:
                self.re_db.rpush("proxies", proxy.split("//")[-1])
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        print("Error from %s" % (__file__,))
        for ex in exception.args:
            print("\033[0;31m{0}\033[0m".format(ex))
        # proxy = self.get_ip
        # request.meta['proxy'] = proxy
        # request.meta['download_timeout'] = 15
        # print("-" * 10, "切换代理: ", proxy, "-" * 10)
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def spider_closed(self, spider):
        self.re_db.close()
        print("-" * 15, "关闭库成功", "-" * 15)
