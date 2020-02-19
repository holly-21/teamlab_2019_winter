# week 3 _ Web Bootcamp
html, css등을 이용해 웹 front-end 제작

## 학습 결과
* 크롤링 핵심코드
```
# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
# 웹페이지 갖고 오기
res = requests.get('https://news.v.daum.net/v/20200208060031346')
# 웹 페이지 파싱하기
soup = BeautifulSoup(res.content, 'html.parser')
# 필요한 데이터 추출하기
mydata = soup.find('h3')
mydata.get_text()
```
결과 : '유통가 "중국과 질긴 악연?"..사드 악몽 벗어날 만하니 \'코로나 쇼크\''

* html을 이용한 크롤링
```
from bs4 import BeautifulSoup
html = """
<html>
    <body>
        <h1 id='title'>[1]크롤링이란?</h1>
        <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p>
        <p id='body align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# 태그로 검색하는 방법
data = soup.find('h1')
data_2 = soup.find('p')
print(data)
print(data.string)
print(data.get_text())
```

* css를 이용한 크롤링
  css 언어를 이용할 때는 select를 사용하여 원하는 정보를 찾는다
  아래 코드에서 select(".tit_view")에서 '.'은 class를 나타낸다. 따라서 class가 "tit_view"라는 것을 의미한다.
  또는 selector를 이용항 select("#cSub > div > h3")로 표현할 수도 있다.
  
```
import requests
from bs4 import BeautifulSoup

site_list = ["https://entertain.v.daum.net/v/20200209090702953"]
for site in site_list:
    res = requests.get(site)
    soup = BeautifulSoup(res.content,"html.parser")

    mydata = soup.select(".tit_view")
    for item in mydata:
        print(item.get_text())
 ```
 결과 : '슈돌' 윌벤져스, 치과 방문..'겁에 질린' 벤틀리→'허세' 윌리엄 [Oh!쎈 컷]
 
 
 

## html,css로 구축한 front-end (

* 메인 페이지(홈 화면)
![메인 페이지](https://user-images.githubusercontent.com/48376471/74810296-6a976b80-5332-11ea-9762-c7b6046d1af2.png)

* 페이지의 기능을 설명하는 화면
![페이지설명](https://user-images.githubusercontent.com/48376471/74810388-99addd00-5332-11ea-99dc-372d75c0fdb2.png)

* 검색 화면
![검색 화면](https://user-images.githubusercontent.com/48376471/74810396-9e729100-5332-11ea-9430-380a4db9ab6a.png)

* 전체 웹툰 정보를 볼 수 있는 화면
![전체 웹툰 리스트](https://user-images.githubusercontent.com/48376471/74810433-b34f2480-5332-11ea-826a-da924014a9a3.png)


