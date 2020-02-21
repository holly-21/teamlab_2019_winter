# week 6 _ AWS Bootcamp
aws를 사용하여 지금까지 만들었던 시스템을 연결하는 것을 목표로 한다.

## 참고 자료
[[Deploy] Django 프로젝트 배포하기 - 1. AWS](https://nachwon.github.io/django-deploy-1-aws/), 2016.10.26

<br>

## AWS에 장고 배포

### AWS 인스턴스 생성
![AWS](https://user-images.githubusercontent.com/48376471/74895756-dda5ee00-53d5-11ea-94ff-e6912138ed50.png)

### mysqldump를 이용하여 데이터베이스를 원격저장소로 갖고 오기
```
mysqldump -uroot -p WT_DB>WT_DB.sql

scp -i pem파일위치 -r /home/wonyoung/WT_DB.sql ubuntu@내 퍼블릭 DNS

mysql -u root -p --database=WT_DB < WT_DB.sql
```

### 웹사이트에 원격접속하는 방법
aws 인스턴스 작동
원격서버에 접속
python manage.py runserver 0:8080
퍼블릭 DNS로 웹사이트 접속하기

[WEBTOON SEARCH 접속하기](http://ec2-15-165-160-214.ap-northeast-2.compute.amazonaws.com:8080/)

<br>

## crontab을 이용한 주기적 크롤링 실행 자동화

1. 주기적으로 크롤링을 자동으로 실행하기 위해서는 pymysql을 사용하여 데이터베이스를 저장한다.
장고 settings.py에 pymysql을 실행하기위해 다음과 같이 입력한다.
```
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()
```

2. 장고 settings.py의 ALLOWED_HOSTS에 '127.0.0.1'을 추가로 입력한다.

3. AWS 서버에 crontab -e를 입력하여 crontab을 세팅한다.
```
10 0 * * 1 /home/wonyoung/workspace/total_cron.py >> /home/wonyoung/workspace/cron.log
```
위와 같은 내용을 crontab 세팅창 하단에 입력한다. <br>
코드 해석 : 매주 월요일마다 오전 0시 10분에 total_cron.py파일을 자동으로 실행하도록 예약한다. 이 실행에 대한 로그를 cron.log에 기록한다.

4. 입력이 잘됐는지 확인하기 위해 서버창에 crontab -l을 입력하고 다음과 같은 결과를 확인할 수 있다.
![crontab-l](https://user-images.githubusercontent.com/48376471/74997015-74d37a00-5498-11ea-91a5-e357e824b81d.png)
