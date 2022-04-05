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


op = Options()
op.add_experimental_option('prefs',{'download.default_directory':r'C:\file_gonggo'})
driver = webdriver.Chrome(r"C:\Users\PC\chromedriver.exe",options=op)
search = input('검색어를 입력하세요 : ')
url = 'https://www.mss.go.kr/site/smba/ex/bbs/List.do?cbIdx=310'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
elem = driver.find_element_by_id('searchKey').send_keys(search)
driver.find_element_by_css_selector('#contents_inner > div > div.search_box.search_box-1 > div.search_form.search_form-1 > div > button').click()
elements = driver.find_elements_by_css_selector('#contents_inner > div > table > tbody > tr')
#contents_inner > div > table > tbody > tr:nth-child(1) > td.mobile > a > div.subject
for j in range(2,11):
    for i in range(1,11):
        pead_path = '/html/body/div[2]/form/div/div/table/tbody/tr[{}]'.format(i)
        a_tag = driver.find_element_by_xpath(pead_path).text
        pead_path3 = '/html/body/div[2]/form/div/div/table/tbody/tr[{0}]/td[{1}]/a'.format(i,5)
        c_tag = driver.find_element_by_xpath(pead_path3).click()
        print(a_tag)
        driver.implicitly_wait(3)
        print("\n")   
        if(i==10):
            pead_path2 = '/html/body/div[2]/form/div/div/div[4]/ul/li[{}]/a'.format(j)
            b_tag = driver.find_element_by_xpath(pead_path2).click()