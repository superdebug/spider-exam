create database spiderdb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use spiderdb;
create table news 
(
title varchar(100),
link varchar(60) primary key,
desc_text varchar(60),
content text,
web1 int NOT NULL DEFAULT 0,
web2 int NOT NULL DEFAULT 0,
web3 int NOT NULL DEFAULT 0,
web4 int NOT NULL DEFAULT 0,
web5 int NOT NULL DEFAULT 0,
create_time timestamp NOT NULL DEFAULT NOW())
ENGINE=InnoDB DEFAULT CHARSET=utf8;

