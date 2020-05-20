# -*- coding: utf-8 -*-
# : Time    : 2020/05/15
__author__ = "Miman"


from fake_useragent import UserAgent
import requests
try:
    import cookielib
except Exception:
    import http.cookiejar as cookielib


headers = {
    'User-Agent': UserAgent().random,
}

session = requests.Session()
session.cookies = cookielib.LWPCookieJar("baidu_cookies")

def login_with_cookie():
    try:
        session.cookies.load(ignore_discard=True)
        if len(session.cookies) < 20:
            raise ValueError("cookie can't be loaded")
    except Exception as e:
        print(e)
        status_code = session.get(url="http://www.baidu.com", headers=headers).status_code
        if status_code == 200:
            session.cookies.save(ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
    login_with_cookie()
