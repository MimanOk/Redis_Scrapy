# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class UserPipeline(object):
    def process_item(self, item, spider):
        # print("name: ", item['name'],
        #       "headline: ", item['headline'],
        #       "gender: ", item['gender'],
        #       "description: ", item['description'],
        #       "business: ", item['business'],
        #       "locations: ", item['locations'],
        #       sep='\n')

        return item

class MeiTuPipeline(object):
    def process_item(self, item, spider):
        for i in item:
            print("\033[0;32m%s -- %s\033[0m" % (i, item[i]))
