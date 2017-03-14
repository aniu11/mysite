#encoding=utf-8

import requests

proxies = {"http":"http://172.17.18.80:8080",}
requests.get("http://excample.org",proxies=proxies)