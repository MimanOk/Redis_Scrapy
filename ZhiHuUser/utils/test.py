# -*- coding: utf-8 -*-
# : Time    : 2020/04/30
__author__ = "Miman"

import os

def run():
    print(os.getcwd())
    print(os.path.dirname(os.path.abspath(__file__)))

print(os.path.exists("D://Desktop"))
# import requests
# from fake_useragent import UserAgent
#
# headers = {
#     'Host': 'www.521609.com',
#     'Referer': 'http://www.521609.com',
#     'User-Agent': UserAgent().random
# }
#
# def get_html(url):
#     response = requests.get(url=url, headers=headers)
#     print(response.text)
#
# if __name__ == '__main__':
#     get_html("http://www.521609.com")