CREATE DATABASE EIMS DEFAULT CHARACTER SET utf8;
LOAD DATA LOCAL INFILE 'EIMS/data/企业基础信息表.csv' INTO TABLE company_company fields terminated by ',' optionally enclosed by '"' escaped by '"';
LOAD DATA LOCAL INFILE 'EIMS/data/企业人员表.csv' INTO TABLE human_serving fields terminated by ',' optionally enclosed by '"' escaped by '"';
LOAD DATA LOCAL INFILE 'EIMS/data/企业信息变更表.csv' INTO TABLE company_change fields terminated by ',' optionally enclosed by '"' escaped by '"';
LOAD DATA LOCAL INFILE 'EIMS/data/商标注册信息表.csv' INTO TABLE company_trademark fields terminated by ',' optionally enclosed by '"' escaped by '"';
LOAD DATA LOCAL INFILE 'EIMS/data/商标分类表.csv' INTO TABLE company_classification fields terminated by ',' optionally enclosed by '"' escaped by '"';
