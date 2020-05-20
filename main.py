# -*- coding: utf-8 -*-
# : Time    : 2020/04/15

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "meitu"])