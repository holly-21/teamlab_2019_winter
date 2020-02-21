from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib
import re
from urllib.request import urlopen
import selenium

import csv
import pymysql
import pandas as pd


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
        hrefs_lists.append(h)

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
        each_url = 'https://comic.naver.com' + w_detail['url'][i]

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


def sql_db():
    # mysql DB에 접속
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='WT_DB', charset='utf8')

    cursor = db.cursor(pymysql.cursors.DictCursor)

    # 기존 DB 삭제
    dele = "DELETE FROM WT_DB.WT"
    cursor.execute(dele)
    db.commit()

    # csv파일 읽어오기
    csv_data = pd.read_csv('webtoonDetail_list.csv', index_col=False)

    # 새 DB 불러오기
    sql = "INSERT INTO WT(wt_date, wt_url, wt_title, wt_writer, wt_rate, wt_genre,wt_age ) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    for raw in csv_data.values:
        cursor.execute(sql, list(raw)[1:])

    db.commit()
    cursor.close()


if __name__ == '__main__':
    # 웹드라이브 열기
    driver = webdriver.Chrome('./chromedriver')
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

    # 요일별 각 웹툰으로 들어가기
    each_url = 'https://comic.naver.com' + w_detail['url'][0]
    driver.get(each_url)
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    # 요일별 전체웹툰 정보와 각 웹툰 정보 합치기
    w_detail.update(get_details())

    df = pd.DataFrame(w_detail)

    driver.close()

    # csv로 저장
    df.to_csv("webtoonDetail_list.csv", index=False)

    sql_db()