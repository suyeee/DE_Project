create database insta;
show databases;
use insta;

drop table insta_crawling;

CREATE TABLE insta_crawling
(
id INT PRIMARY KEY AUTO_INCREMENT,
date DATE not null,
likes VARCHAR(25) NOT NULL,
view VARCHAR(25) NOT NULL,
hashtags TEXT,
content TEXT NOT NULL
);