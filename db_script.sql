-- SQL script to create tables

-- Drop Tables
DROP TABLE IF EXISTS USER; 
DROP TABLE IF EXISTS RESTAURANT; 
DROP TABLE IF EXISTS WAITLIST;
-- DROP TABLE IF EXISTS NAME; 
-- DROP TABLE IF EXISTS LOCATION; 
-- DROP TABLE IF EXISTS PRICE; 
-- DROP TABLE IF EXISTS CATEGORY; 

-- Create user table
CREATE TABLE USER (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT unique NOT NULL,
  pswd TEXT NOT NULL
);

-- Create restaurant table
-- Attributes: ID, name, Location, contact, open, price, category
CREATE TABLE RESTAURANT (
    manager_id int NOT NULL,
    rest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
	loc TEXT NOT NULL,
	contact TEXT NOT NULL,
	hour TEXT NOT NULL,
    price TEXT NOT NULL,
	category TEXT NOT NULL,
    FOREIGN KEY (manager_id) REFERENCES user (id)
);

-- Create waitlist table
-- Attributes: id, placement, name, size, time
CREATE TABLE WAITLIST (
    list_id int NOT NULL,
    cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cust TEXT NOT NULL,
    size int NOT NULL,
    start_time time NOT NULL,
    FOREIGN KEY (list_id) REFERENCES RESTAURANT(rest_id)
);

-- -- Application for Index Table Pattern
-- -- Creating Index Tables
-- -- by name
-- CREATE TABLE NAME (
--     name TEXT NOT NULL PRIMARY KEY,
--     rest_id int NOT NULL,
--     manager_id int NOT NULL,
-- 	location TEXT NOT NULL,
-- 	contact TEXT NOT NULL,
-- 	open TEXT NOT NULL,
--     price TEXT NOT NULL,
-- 	category TEXT NOT NULL,
--     FOREIGN KEY (manager_id) REFERENCES user (id)
-- );
-- -- by Location
-- CREATE TABLE LOCATION (
--     Location TEXT NOT NULL PRIMARY KEY,
--     rest_id int NOT NULL,
--     name TEXT NOT NULL,
-- 	contact TEXT NOT NULL,
-- 	open TEXT NOT NULL,
--     price TEXT NOT NULL,
-- 	category TEXT NOT NULL,
--     FOREIGN KEY (manager_id) REFERENCES user (id)
-- );
-- -- Search by price
-- CREATE TABLE PRICE (
--     price TEXT NOT NULL PRIMARY KEY,
--     rest_id int NOT NULL,
--     name TEXT NOT NULL,
-- 	Location TEXT NOT NULL,
-- 	contact TEXT NOT NULL,
-- 	open TEXT NOT NULL,
-- 	category TEXT NOT NULL,
--     FOREIGN KEY (manager_id) REFERENCES user (id)
-- );
-- -- by category
-- CREATE TABLE CATEGORY (
--     category TEXT NOT NULL PRIMARY KEY,
--     rest_id int NOT NULL,

--     name TEXT NOT NULL,
-- 	Location TEXT NOT NULL,
-- 	contact TEXT NOT NULL,
-- 	open TEXT NOT NULL,
--     price TEXT NOT NULL,
--     FOREIGN KEY (manager_id) REFERENCES user (id)
-- );