from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from gensim.summarization.summarizer import summarize
from newspaper import Article
import requests
from PIL import Image
import urllib.request
import time
from io import BytesIO

driver = webdriver.Chrome(r"C:\Users\PC\chromedriver.exe")
search = input('검색어를 입력하세요 : ')
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+search
url2 = 'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword='+search
url3 = "https://search.pstatic.net/common/?src=https%3A%2F%2Fimgnews.pstatic.net%2Fimage%2Forigin%2F108%2F2022%2F03%2F29%2F3039729.jpg&type=ff264_180&expire=2&refresh=true"

b = input('뉴스 or 블로그');
req = urllib.request.Request(url3, headers = {"User-Agent" : "Mozilla/5.0"})
res = urllib.request.urlopen(req).read()


if(b=='뉴스'):
    driver.get(url)
if(b=='블로그'):
    driver.get(url2)

soup = BeautifulSoup(driver.page_source, 'html.parser')

title = soup.select('a.news_tit')
title2 = soup.select('a.desc_inner')
if(b=='뉴스'):
    for i in title:
        a_tag = i.get_text()
        print("\n",a_tag)
        print(i.attrs['href'])
        urlopen_img = Image.open(BytesIO(res))
        driver,quit()

if(b=='블로그'):
    for j in title2:
        b_tag = j.get_text()
        print("\n",b_tag)
        print(j.attrs['ng-href'])
        driver,quit()
    #sp_nws1 > div > div > a
c = input('URL 입력')
driver.get(c)
news = Article(c)
news.download()

news.parse()
print(summarize(news.text, word_count=50))