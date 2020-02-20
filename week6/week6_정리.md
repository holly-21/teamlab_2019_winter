# week 6 _ AWS Bootcamp
aws를 사용하여 지금까지 만들었던 시스템을 연결하는 것을 목표로 한다.

## 참고 자료
[[Deploy] Django 프로젝트 배포하기 - 1. AWS](https://nachwon.github.io/django-deploy-1-aws/),2016.10.26


### AWS 인스턴스 생성
![AWS](https://user-images.githubusercontent.com/48376471/74895652-928bdb00-53d5-11ea-96bc-5f8a7caef767.png)

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

[WEBTOON SEARCH 접속 주소](http://ec2-15-165-160-214.ap-northeast-2.compute.amazonaws.com:8080/)
