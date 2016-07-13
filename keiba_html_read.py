# -*- coding: utf-8 -*-
# python 2.7
import lxml.html
import datetime
import json
import requests
import re
import os
import sys
import glob
from bs4 import BeautifulSoup
'''
def getKB():
    url = 'http://minkabu.jp/top/stock_news'
    tree = lxml.html.parse(url)
    contents = map(lambda html: html.text, tree.xpath('//*[@id="ajax_update_stock_news"]//td'))
    contents2=map(lambda html: html.text, tree.xpath('//*[@id="ajax_update_stock_news"]//td/a'))
    for i in range(0,len(contents)-1,1):
        if contents[i]==None:
            contents[i]=0
        else:
            contents[i]=contents[i].encode('utf-8')
    j=0
    res=[]
    for i in range(2,len(contents)-1,5):
        if contents[i+4]==0:
            j=j+1
        else:
            update_date=contents[i].replace('/','-')
            corp_date=contents[i+2].replace('/','-')
            hold=contents[i+4].split(':')
            corp_rate=float(hold[1])/float(hold[0])
            corp_name=contents2[j].encode('utf-8')
            corp_name=re.findall('\([0-9]+[0-9]+[0-9]+[0-9]+\)', corp_name)
            corp_name=re.findall('[0-9]+[0-9]+[0-9]+[0-9]+', corp_name[0])
            corp_name=corp_name[0]
            temp=str(corp_name)
            temp2=corp_date.replace('-','')
            key_id=temp+temp2
            j=j+1
            jsondata={'update_date':update_date, 'corp_date':corp_date, 'corp_rate':corp_rate, 'corp_name':corp_name,'key_id':key_id}
            res.append(jsondata)

    print(res)
    return res


def postDB(post_data):
    response = requests.post('http://xxxxxxx', post_data)
'''
def get_file_name():
    files=[os.path.basename(r) for r in glob.glob('/Users/HashimotoYoshinori/Desktop/keiba_data/keiba_data/netkeiba-scraper/html/*.html')] #ここを変える
    return files

                             
if __name__ == '__main__':
    files=get_file_name()
    os.chdir('./html')
    for file in files:
        print file
        f=open(file)
        htmltxt=f.read()
        soup=BeautifulSoup(htmltxt,'html.parser') #これでhtmlが綺麗になる
        contents=soup.select('div#contents_liquid td > table > tbody') #書き方勉強
        print len(contents)
        print contents
        sys.exit()　#とりあえずテストなので

'''
    rows=getKB()
    for i in range(0,len(rows),1):
        tmp=rows[i]
        postDB(tmp)
'''