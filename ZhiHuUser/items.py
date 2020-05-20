# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    age = Field()
    gender = Field()
    headline = Field()
    description = Field()
    business = Field()
    locations = Field()


class MeiTuItem(Item):
    image_desc = Field()
    image_url = Field()
