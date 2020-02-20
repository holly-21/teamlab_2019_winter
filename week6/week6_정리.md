# week 6 _ AWS Bootcamp
aws를 사용하여 지금까지 만들었던 시스템을 연결하는 것을 목표로 한다.

## 참고 자료
[[Deploy] Django 프로젝트 배포하기 - 1. AWS](https://nachwon.github.io/django-deploy-1-aws/),2016.10.26


## mysqldump를 이용하여 데이터베이스를 원격저장소로 갖고 오기
```
mysqldump -uroot -p WT_DB>WT_DB.sql

scp -i pem파일위치 -r /home/wonyoung/WT_DB.sql ubuntu@내 퍼블릭 DNS

mysql -u root -p --database=WT_DB < WT_DB.sql
```
