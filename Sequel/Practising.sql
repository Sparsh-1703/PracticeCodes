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

-- CREATE TABLE people (
-- 	name VARCHAR(100),
--     birthdate DATE,
--     birthtime TIME,
--     birthdt DATETIME
-- );
-- INSERT INTO people (name, birthdate, birthtime, birthdt)
-- VALUES ('Elton', '2000-12-25', '11:00:00', '2000-12-25 11:00:00');
--  
-- INSERT INTO people (name, birthdate, birthtime, birthdt)
-- VALUES ('Lulu', '1985-04-11', '9:45:10', '1985-04-11 9:45:10');
--  
-- INSERT INTO people (name, birthdate, birthtime, birthdt)
-- VALUES ('Juan', '2020-08-15', '23:59:00', '2020-08-15 23:59:00');
-- select * from people;
-- SELECT CURTIME();
-- SELECT CURDATE();
-- SELECT NOW();
-- INSERT INTO people (name, birthdate, birthtime, birthdt)
-- VALUES ('Hazel', CURDATE(), CURTIME(), NOW());
-- SELECT birthdate, DAY(birthdate), DAYOFWEEK(birthdate), DAYOFYEAR(birthdate) FROM people;
-- SELECT birthdate, MONTHNAME(birthdate), YEAR(birthdate) FROM people;
-- SELECT birthtime, HOUR(birthtime), MINUTE(birthtime) FROM people;
-- SELECT birthdt, MONTH(birthdt), DAY(birthdt), HOUR(birthdt), MINUTE(birthdt) FROM people;
-- SELECT birthdate, DATE_FORMAT(birthdate, '%a %b %D') FROM people;
-- SELECT birthdt, DATE_FORMAT(birthdt, '%H:%i') FROM people;
-- SELECT birthdt, DATE_FORMAT(birthdt, 'BORN ON: %r') FROM people;
 
-- CREATE TABLE captions(
--   text VARCHAR(150),
--   created_at TIMESTAMP default CURRENT_TIMESTAMP,
--   updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );

-- SELECT * FROM people WHERE birthtime BETWEEN CAST('12:00:00' AS TIME) AND CAST('16:00:00' AS TIME);
-- SELECT * FROM people WHERE HOUR(birthtime) BETWEEN 12 AND 16;

-- CREATE TABLE contacts (
-- 	name VARCHAR(100) NOT NULL,
--     phone VARCHAR(15) NOT NULL UNIQUE
-- );
--  
-- INSERT INTO contacts (name, phone)
-- VALUES ('billybob', '8781213455');
-- -- -- This insert would result in an error:
-- INSERT INTO contacts (name, phone)
-- VALUES ('billybob', '8781213455');

-- CREATE TABLE users (
-- 	username VARCHAR(20) NOT NULL,
--     age INT CHECK (age > 0)
-- );
--  
-- CREATE TABLE palindromes (
--   word VARCHAR(100) CHECK(REVERSE(word) = word)
-- )
-- CREATE TABLE houses (
--   purchase_price INT NOT NULL,
--   sale_price INT NOT NULL,
--   CONSTRAINT sprice_gt_pprice CHECK(sale_price >= purchase_price));

-- ALTER TABLE users ADD COLUMN employee_count INT NOT NULL DEFAULT 1;
-- ALTER TABLE users DROP COLUMN employee_count;
-- RENAME TABLE companies to suppliers;
-- ALTER TABLE suppliers RENAME TO users;


-- INSTEAD OF TYPING THIS QUERY ALL THE TIME...
-- SELECT 
--     title, released_year, genre, rating, first_name, last_name
-- FROM
--     reviews
--         JOIN
--     series ON series.id = reviews.series_id
--         JOIN
--     reviewers ON reviewers.id = reviews.reviewer_id;
 
-- WE CAN CREATE A VIEW:
-- CREATE VIEW full_reviews AS
-- SELECT title, released_year, genre, rating, first_name, last_name FROM reviews
-- JOIN series ON series.id = reviews.series_id
-- JOIN reviewers ON reviewers.id = reviews.reviewer_id;
--  
 -- NOW WE CAN TREAT THAT VIEW AS A VIRTUAL TABLE 
 -- (AT LEAST WHEN IT COMES TO SELECTING)
-- SELECT * FROM full_reviews;
