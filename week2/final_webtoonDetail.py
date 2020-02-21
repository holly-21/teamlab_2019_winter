from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib
import re
from urllib.request import urlopen
import selenium
from selenium.webdriver.chrome.options import Option


def get_url_list():
    urls = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    URL_list = []
    for i in range(7):
        url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + urls[i]
        URL_list.append(url)

    return URL_list


def get_whole_detail():
    soup = BeautifulSoup(source, 'html.parser')

    # 오늘 날짜
    date = soup.find("h3").text

    soup = soup.find('div', {'class': 'list_area daily_img'})

    # 웹툰별 url 받아오기
    hrefs = soup.select("dt > a[href]")
    for hre in hrefs:
        h = hre.get('href')
        hr = 'https://comic.naver.com' + h
        hrefs_lists.append(hr)

    # 웹툰별 제목 받아오기
    titles = soup.select("dt > a[title]")
    for tit in titles:
        t = tit.get('title')
        titles_lists.append(t)

    # 웹툰별 작가 받아오기
    writers = soup.select("dd[class=desc]")
    for writ in writers:
        w = writ.text.replace('\n', '')
        writers_lists.append(w)

    # 웹툰별 평점 받아오기
    rates = soup.select("div[class=rating_type] > strong")
    for rat in rates:
        r = rat.text
        rates_lists.append(r)

        # 각 웹툰마다 날짜 기입
        date_lists.append(date)

    whole_detail = {'date': date_lists, 'url': hrefs_lists, 'title': titles_lists, 'writer': writers_lists,
                    'rate': rates_lists}

    return whole_detail


# 각 웹툰의 장르,이용가 받아오기
def get_details():
    genres_lists = []
    ages_lists = []

    for i in range(len(w_detail['url'])):
        each_url = w_detail['url'][i]

        driver.get(each_url)
        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')

        genre = soup.select("p[class=detail_info] > span[class=genre]")
        for gen in genre:
            g = gen.text
            genres_lists.append(g)

        age = soup.select("p[class=detail_info] > span[class=age]")
        for a in age:
            a = a.text
            ages_lists.append(a)

        detail_list = {'genre': genres_lists, 'age': ages_lists}

    return detail_list


if __name__ == '__main__':
    # 웹드라이브 열기
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options, executable_path='/home/ubuntu/workspace/workspace/chromedriver')
    driver.implicitly_wait(3)

    date_lists = []
    hrefs_lists = []
    titles_lists = []
    writers_lists = []
    rates_lists = []

    for u in range(7):
        # 요일별 전체 웹툰 정보 받아오기
        driver.get(get_url_list()[u])
        source = driver.page_source

        w_detail = get_whole_detail()

    driver.implicitly_wait(1)

    # 요일별 전체웹툰 정보와 각 웹툰 정보 합치기
    w_detail.update(get_details())

    driver.implicitly_wait(1)

    df = pd.DataFrame(w_detail)

    driver.close()

    # csv로 저장
    df.to_csv("webtoonDetail_list.csv", index=False)
