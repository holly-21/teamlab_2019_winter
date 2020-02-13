import selenium
import time
from selenium import webdriver
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

# 드라이버 열기
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://comic.naver.com/webtoon/weekday.nhn')

def get_info():
    # 각 요일의 전체 웹툰의 세부정보
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    wholewebs = soup.find('ul', {'class': 'img_list'})
    daywebs = wholewebs.find_all('dl')

    alist = []
    for d in daywebs:
        a = (d.text).replace('\n', ' ').replace('전체보기', '').strip()
        alist.append(a)

    return alist


# 요일별 페이지 들어가기
urls = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
all_info = []
days_list = []

for i in range(7):
    url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + urls[i]
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # 웹툰 정보 받아오기
    what_day = soup.find('h3', {'class': 'sub_tit'}).text
    days_list.append(what_day)
    all_info.append(get_info())

fin_table = pd.DataFrame(all_info).T
fin_table.columns = days_list

# 엑셀로 저장
fin_table.to_excel("webtoon_list.xlsx")