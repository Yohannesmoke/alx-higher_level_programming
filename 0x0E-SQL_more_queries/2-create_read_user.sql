-- create database hbtn_0d_2
-- user user_0d_2 and password user_0d)2_pwd
-- privilage select
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.* TO user_0d_2;
