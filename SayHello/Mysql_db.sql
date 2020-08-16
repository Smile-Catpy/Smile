SET GLOBAL time_zone = '+8:00';
SET time_zone = '+8:00';

drop database E6B034E9E1772CE9B1617B2616B3E507; #删库
create database E6B034E9E1772CE9B1617B2616B3E507 character set utf8; #创建数据库
use E6B034E9E1772CE9B1617B2616B3E507;
create table F54B0E0D24F33E50879796722009B500
(
    id        BIGINT AUTO_INCREMENT COMMENT '主键列（自增）',
    name      CHAR(20) COMMENT '用户姓名',
    text      CHAR(200) COMMENT '文章',
    timestamp TIMESTAMP COMMENT '发表日期',
    CONSTRAINT pk_id PRIMARY KEY (id)
) engine = innodb;