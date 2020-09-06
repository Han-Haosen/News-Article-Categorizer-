from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import random
import jieba.analyse
import elasticsearch
class News:
    title = ""
    source = ""
    create_time = 0
    comment_count = 0
    article_url = ""
    typeV = ""
    content = ""
    initialized = False
    def __init__(self):
        initialized = True
url="https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&format=json&keyword=%E7%89%B9%E6%9C%97%E6%99%AE&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1591923542581&_signature=DzfnbAAgEBDvTFRyAmhz5w82pnAAFHaTWIVlbkPsJLSMz-GqdzbE2Pr.Nlst65cBHor5mEY8XYtcBcrn3FS-CpC7H2Ub.XpWOg4odcqk9jPugCAJg0wIcTicdAlYQhcPBxp&offset="
cookies={
    "cookie":"tt_webid=6717252305459611148; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6717252305459611148; UM_distinctid=16c249a6c884cb-03a8ff7faa9541-345b4871-144000-16c249a6c89108; CNZZDATA1259612802=1075337272-1563979517-https%253A%252F%252Fwww.sogou.com%252F%7C1563979517; __tasessionId=6aeeg14nz1563982196051; csrftoken=d4074b1c3f4159bba519340770901fdf; s_v_web_id=e95f92e1d96dbeace08ab532f0156ca8"
}
combinedTitle = ""
urlArticle = []
for i in range(0,100,20):
    urlTemp = url + str(i)
    rs=requests.get(urlTemp,cookies=cookies) 
    responsejson = json.loads(rs.text)
    for individual in responsejson['data']:
        if(individual['app_info'] == None):
            continue
        else:
            if(individual.get('source') == None):
                continue
            else:
                tempNews = News()
                tempNews.title = individual['title']
                tempNews.source = individual['source']
                tempNews.create_time = individual.get('create_time')
                tempNews.comment_count = individual.get('comment_count')
                tempNews.article_url = individual.get('article_url')
                if(individual.get('tag') == 'video_domestic'):
                    tempNews.typeV = 'video'
                urlArticle.append(tempNews)
                if(int(individual['create_time']) >= 1577840400):
                    combinedTitle += individual['title']
for i in urlArticle:
    print(i.title)
    print(i.source)
    print(i.create_time)
    print(i.comment_count)
print(jieba.analyse.textrank(combinedTitle, topK=10,withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')))

        

