from bs4 import BeautifulSoup
import requests

# 웹페이지 열기
res = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(res.text,'html.parser')
res.close()

# 모든 요일별 웹툰 추출
data_list = soup.find_all('div', {'class':'col_inner'})

week_lists = []

# 제목 추출
for data in data_list:
    title = data.find_all('a', {'class':'title'})
    titles = [t.text for t in title]
    week_lists.append(titles)

# 엑셀 파일에 정보 저장
import pandas as pd
import numpy as np
from openpyxl import Workbook

df = pd.DataFrame.from_records(week_lists)

df.to_excel('webtoonTitle.xlsx')
