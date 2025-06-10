-- show databases;
-- create database DB1;
-- use db1;

-- CREATE TABLE employees (
-- id INT AUTO_INCREMENT PRIMARY KEY,
-- last_name VARCHAR(100) NOT NULL,
-- first_name VARCHAR(100) NOT NULL,
-- middle_name VARCHAR(100),
-- age INT NOT NULL,
-- current_status VARCHAR(100) NOT NULL DEFAULT 'employed');

-- INSERT INTO employees (last_name, first_name, middle_name, 
-- age, current_status) VALUES ('Smith', 'John', 'A.', 32, 'employed'),
-- ('Doe', 'Jane', NULL, 28, 'on leave'),
-- ('Patel', 'Raj', 'Kumar', 45, 'employed'),
-- ('Lee', 'Sara', NULL, 37, 'terminated');

-- desc employees;
-- select * from employees;



-- CREATE TABLE cats
-- (
-- cat_id INT AUTO_INCREMENT,
-- name VARCHAR(100),
-- breed VARCHAR(100),
-- age INT,
-- PRIMARY KEY (cat_id)
-- );
-- INSERT INTO cats(name, breed, age)
-- VALUES ('Ringo', 'Tabby', 4),
-- ('Cindy', 'Maine Coon', 10),
-- ('Dumbledore', 'Maine Coon', 11),
-- ('Egg', 'Persian', 4),
-- ('Misty', 'Tabby', 13),
-- ('George Michael', 'Ragdoll', 9),
-- ('Jackson', 'Sphynx', 7);

-- select name, breed from cats;
-- select * from cats where age = 4 and name = 'egg';
-- select name AS kittens from cats;

-- SET SQL_SAFE_UPDATES = 0;
-- update employees set current_status = 'Laid Off', last_name = 'lmao';

-- select concat_ws(' ',first_name, last_name) as full_name from employees;
-- select * from employees;
-- update cats set age = 14 where name = 'misty';
-- delete from cats where name = 'egg';
-- select * from cats;

-- select substring("hello world", -2, 3);
