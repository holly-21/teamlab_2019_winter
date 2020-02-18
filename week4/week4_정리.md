# week 4 _ Database Bootcamp
mysql을 이용하여 데이터를 database화하는 것을 목표로 한다.


* mysql DB 생성 코드
```
CREATE database IF NOT exists WT_DB;
USE WT_DB;

DROP TABLE IF EXISTS WT_DB.WT, WT_DB.USERS, WT_DB.SEARCH;

CREATE TABLE IF NOT EXISTS WT_DB.WT(
	webtoon_ID int not null auto_increment,
    wt_date varchar(50) not null,
    wt_url varchar(100) not null,
    wt_title varchar(50) not null,
    wt_writer varchar(50) not null,
    wt_rate float null,
    wt_genre varchar(50) not null,
    wt_age varchar(30) not null,
    primary key(webtoon_ID)
    );

CREATE TABLE IF NOT EXISTS WT_DB.USERS(
	user_ID int not null auto_increment,
    user_name varchar(50) not null,
    user_pwd varchar(50) not null,
    primary key(user_ID)
    );
    
CREATE TABLE IF NOT EXISTS WT_DB.SEARCH(
	search_ID int not null auto_increment,
    search_info varchar(100) null,
    webtoon_ID int not null,
    user_ID int not null,
    primary key(search_ID),
    foreign key(webtoon_ID)
		references WT(webtoon_ID)
        on delete no action
        on update no action,
	foreign key(user_ID)
		references USERS(user_ID)
        on delete no action
        on update no action
	);
  ```
  
  
 * csv 파일을 mysql에 연동하는 코드
 ```
LOAD DATA LOCAL INFILE 'C:\Users\holly\Documents\teamlab_2019_winter\week2\webtoonDetail_list.csv'
INTO TABLE WT_DB.WT
CHARACTER SET utf8
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
```


* 연동 완료 시 결과
![img_mysql_1](https://user-images.githubusercontent.com/48376471/74754973-c40d8500-52b5-11ea-8c2d-62a72968bfe5.png)


* mysql의 ERD
![img_mysql_2](https://user-images.githubusercontent.com/48376471/74755121-02a33f80-52b6-11ea-8a53-9b57e573b8a7.png)
