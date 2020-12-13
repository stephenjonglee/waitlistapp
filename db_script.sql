-- SQL script to create tables

-- Drop Tables
DROP TABLE IF EXISTS USER; 
DROP TABLE IF EXISTS RESTAURANT; 
DROP TABLE IF EXISTS WAITLIST; 
DROP TABLE IF EXISTS NAME; 
DROP TABLE IF EXISTS LOCATION; 
DROP TABLE IF EXISTS PRICE; 
DROP TABLE IF EXISTS CATEGORY; 

-- Create user table
CREATE TABLE USER (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT unique NOT NULL,
  pswd TEXT NOT NULL
);

-- Create restaurant table
-- Attributes: ID, name, Location, contact, open, price, category
CREATE TABLE RESTAURANT (
    rest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manager_id int NOT NULL,
    title varchar(100) NOT NULL,
	loc varchar(100) NOT NULL,
	contact varchar(100) NOT NULL,
	hour varchar(100) NOT NULL,
    price varchar(100) NOT NULL,
	category varchar(100) NOT NULL,
    FOREIGN KEY (manager_id) REFERENCES user (id)
);

-- Create waitlist table
-- Attributes: id, placement, name, size, time
CREATE TABLE WAITLIST (
    cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id int NOT NULL,
    cust varchar(100) NOT NULL,
    size int NOT NULL,
    start_time time NOT NULL,
    FOREIGN KEY (list_id) REFERENCES RESTAURANT(rest_id)
);

-- -- Application for Index Table Pattern
-- -- Creating Index Tables
-- -- by name
-- CREATE TABLE NAME (
--     name varchar(100) NOT NULL PRIMARY KEY,
--     rest_id int NOT NULL,
--     manager_id int NOT NULL,
-- 	location varchar(100) NOT NULL,
-- 	contact varchar(100) NOT NULL,
-- 	open varchar(100) NOT NULL,
--     price varchar(100) NOT NULL,
-- 	category varchar(100) NOT NULL,
--     FOREIGN KEY (manager_id) REFERENCES user (id)
-- );
-- -- by Location
-- CREATE TABLE LOCATION (
--     Location varchar(100) NOT NULL PRIMARY KEY,
--     rest_id int NOT NULL,
--     name varchar(100) NOT NULL,
-- 	contact varchar(100) NOT NULL,
-- 	open varchar(100) NOT NULL,
--     price varchar(100) NOT NULL,
-- 	category varchar(100) NOT NULL,
--     FOREIGN KEY (manager_id) REFERENCES user (id)
-- );
-- -- Search by price
-- CREATE TABLE PRICE (
--     price varchar(100) NOT NULL PRIMARY KEY,
--     rest_id int NOT NULL,
--     name varchar(100) NOT NULL,
-- 	Location varchar(100) NOT NULL,
-- 	contact varchar(100) NOT NULL,
-- 	open varchar(100) NOT NULL,
-- 	category varchar(100) NOT NULL,
--     FOREIGN KEY (manager_id) REFERENCES user (id)
-- );
-- -- by category
-- CREATE TABLE CATEGORY (
--     category varchar(100) NOT NULL PRIMARY KEY,
--     rest_id int NOT NULL,

--     name varchar(100) NOT NULL,
-- 	Location varchar(100) NOT NULL,
-- 	contact varchar(100) NOT NULL,
-- 	open varchar(100) NOT NULL,
--     price varchar(100) NOT NULL,
--     FOREIGN KEY (manager_id) REFERENCES user (id)
-- );