# -*- coding: utf-8 -*-

# Scrapy settings for ZhiHuUser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ZhiHuUser'

SPIDER_MODULES = ['ZhiHuUser.spiders']
NEWSPIDER_MODULE = 'ZhiHuUser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ZhiHuUser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# user_agent #
RANDOM_UA_TYPE = "random"
# end #

# redis settings #
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 0
# end #

# 分布式爬虫设置 #
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用优先级队列调度请求(default)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# 暂停续爬
SCHEDULER_PERSIST = True
# end #

# spider meitu settings #
# MEITU_IMAGE_STORE_PATH = "D://Desktop//images"
MEITU_LOG_PATH = "D://Desktop//images//meitu.log"
MEITU_START_URL = "http://www.521609.com/daxuexiaohua/"
# end #

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ZhiHuUser.middlewares.ZhihuuserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'ZhiHuUser.middlewares.DownloadMiddleware': 1,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    # 'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
    # 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 10,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    #    'scrapy.extensions.telnet.TelnetConsole': None,
    # 'scrapy.extensions.logstats.LogStats': None,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'ZhiHuUser.pipelines.UserPipeline': 300,
    'ZhiHuUser.pipelines.MeiTuPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 290,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

CLOSESPIDER_TIMEOUT = 0
CLOSESPIDER_PAGECOUNT = 0
CLOSESPIDER_ITEMCOUNT = 0
CLOSESPIDER_ERRORCOUNT = 0

# REDIRECT_ENABLE = False
