from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import random
from jieba import analyse
import jieba.posseg as pseg
stop = [line.strip() for line in open('stop.txt',encoding='utf-8').readlines()]
sports = [line.strip() for line in open('sports.txt',encoding='utf-8').readlines()]
economic = [line.strip() for line in open('economic.txt',encoding='utf-8').readlines()]
education = [line.strip() for line in open('education.txt',encoding='utf-8').readlines()]
politic = [line.strip() for line in open('politic.txt',encoding='utf-8').readlines()]
tfidf = analyse.extract_tags
textrank = analyse.textrank
with open('test.json') as json1:
    data = json.load(json1)
    f = open("results.txt","a")
    for item in data['sports']:
        keywords = tfidf(item['content'])
        f.write(item['content'])
        f.write('\n')
        f.write(str(keywords))
        f.write('\n')
        sportscount = 0
        politiccount = 0
        economiccount = 0
        educationcount = 0
        for i in sports:
            for k in keywords:
                if i == k:
                    sportscount += 1
        for i in politic:
            for k in keywords:
                if i == k:
                    politiccount += 1
        for i in economic:
            for k in keywords:
                if i == k:
                    economiccount += 1
        for i in education:
            for k in keywords:
                if i == k:
                    educationcount += 1
        if(sportscount == 0 and politiccount == 0 and economiccount == 0 and educationcount == 0):
            f.write("其他\n")
        else:
            types = {'体育':sportscount,'财经':economiccount,'教育':educationcount,'政务':politiccount}
            winner = max(types,key=types.get)
            f.write(winner + "\n")
    for item in data['economic']:
        keywords = tfidf(item['content'])
        f.write(item['content'])
        f.write('\n')
        f.write(str(keywords))
        f.write('\n')
        sportscount = 0
        politiccount = 0
        economiccount = 0
        educationcount = 0
        for i in sports:
            for k in keywords:
                if i == k:
                    sportscount += 1
        for i in politic:
            for k in keywords:
                if i == k:
                    politiccount += 1
        for i in economic:
            for k in keywords:
                if i == k:
                    economiccount += 1
        for i in education:
            for k in keywords:
                if i == k:
                    educationcount += 1
        if(sportscount == 0 and politiccount == 0 and economiccount == 0 and educationcount == 0):
            f.write("Others\n")
        else:
            types = {'Sports':sportscount,'Finance':economiccount,'Education':educationcount,'Politics':politiccount}
            winner = max(types,key=types.get)
            f.write(winner + "\n")
    for item in data['misc']:
        keywords = tfidf(item['content'])
        f.write(item['content'])
        f.write('\n')
        f.write(str(keywords))
        f.write('\n')
        sportscount = 0
        politiccount = 0
        economiccount = 0
        educationcount = 0
        for i in sports:
            for k in keywords:
                if i == k:
                    sportscount += 1
        for i in politic:
            for k in keywords:
                if i == k:
                    politiccount += 1
        for i in economic:
            for k in keywords:
                if i == k:
                    economiccount += 1
        for i in education:
            for k in keywords:
                if i == k:
                    educationcount += 1
        if(sportscount == 0 and politiccount == 0 and economiccount == 0 and educationcount == 0):
            f.write("Others\n")
        else:
            types = {'Sports':sportscount,'Finance':economiccount,'Education':educationcount,'Politics':politiccount}
            winner = max(types,key=types.get)
            f.write(winner + "\n")
    for item in data['education']:
        keywords = tfidf(item['content'])
        f.write(item['content'])
        f.write('\n')
        f.write(str(keywords))
        f.write('\n')
        sportscount = 0
        politiccount = 0
        economiccount = 0
        educationcount = 0
        for i in sports:
            for k in keywords:
                if i == k:
                    sportscount += 1
        for i in politic:
            for k in keywords:
                if i == k:
                    politiccount += 1
        for i in economic:
            for k in keywords:
                if i == k:
                    economiccount += 1
        for i in education:
            for k in keywords:
                if i == k:
                    educationcount += 1
        if(sportscount == 0 and politiccount == 0 and economiccount == 0 and educationcount == 0):
            f.write("Others\n")
        else:
            types = {'Sports':sportscount,'Finance':economiccount,'Education':educationcount,'Politics':politiccount}
            winner = max(types,key=types.get)
            f.write(winner + "\n")

       


    
