-- create database book_shop;
-- use book_shop;
-- CREATE TABLE books 
-- 	(
-- 		book_id INT NOT NULL AUTO_INCREMENT,
-- 		title VARCHAR(100),
-- 		author_fname VARCHAR(100),
-- 		author_lname VARCHAR(100),
-- 		released_year INT,
-- 		stock_quantity INT,
-- 		pages INT,
-- 		PRIMARY KEY(book_id)
-- 	);

-- INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
-- VALUES
-- ('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
-- ('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
-- ('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
-- ('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
-- ('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
-- ('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
-- ('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
-- ('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
-- ('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
-- ('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
-- ('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
-- ("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
-- ('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
-- ('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
-- ('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
-- ('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);
-- INSERT INTO books
-- (title, author_fname, author_lname, released_year, stock_quantity, pages)
-- VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256),
-- ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
-- ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);

-- desc books;

-- select * from books ORDER BY author_lname;
-- SELECT book_id, author_fname, author_lname, pages FROM books ORDER BY 2 desc LIMIT 6,2;
-- SELECT book_id, author_fname, author_lname, pages FROM books ORDER BY author_lname, author_fname;
-- ORDER BY author_lname DESC;
-- ORDER BY released_year;

-- SELECT upper(reverse(REPLACE('cheese bread coffee milk', ' ', ' and '))) as reversed_output;
-- SELECT CHAR_LENGTH('Hello World');
-- SELECT CONCAT(SUBSTRING(title, 1, 8), '...') as 'short title' FROM books;
-- SELECT INSERT('Hello Bobby', 6, 0, 'There'); 
-- SELECT LEFT('omghahalol!', 3);
-- SELECT RIGHT('omghahalol!', 4);
-- SELECT REPEAT('ha', 4);
-- SELECT TRIM('  pickle  ');
-- SELECT author_lname FROM books;
-- SELECT DISTINCT author_lname FROM books;
-- SELECT author_fname, author_lname FROM books;
-- SELECT DISTINCT CONCAT(author_fname,' ', author_lname) FROM books;
-- SELECT DISTINCT author_fname, author_lname FROM books;
-- SELECT * FROM books WHERE author_fname LIKE '_a_';
-- SELECT title, author_fname, author_lname, pages FROM books WHERE author_fname LIKE '%da%';
-- To select books with '%' in their title:
-- SELECT * FROM books WHERE title LIKE '%\%%';
-- SELECT COUNT(*) FROM books WHERE title LIKE '%the%';
-- SELECT title, released_year FROM books WHERE released_year = (SELECT MIN(released_year) FROM books);	
-- SELECT author_fname, author_lname, COUNT(*) FROM books GROUP BY author_lname, author_fname;
-- SELECT author_lname, MAX(released_year), MIN(released_year) FROM books GROUP BY author_lname;
-- SELECT 	author_lname, author_fname,	COUNT(*) as books_written, MAX(released_year) AS latest_release,
  -- MIN(released_year)  AS earliest_release FROM books GROUP BY author_lname, author_fname;
-- SELECT author_lname, COUNT(*), SUM(pages) FROM books GROUP BY author_lname;
-- SELECT AVG(released_year) FROM books;
-- SELECT released_year, AVG(stock_quantity), COUNT(*) FROM books GROUP BY released_year;
-- SELECT title, author_lname, released_year FROM books WHERE released_year > 2010 AND author_lname = 'Eggers' AND title LIKE '%novel%';
-- SELECT title, author_lname, released_year FROM books WHERE author_lname='Eggers' OR released_year > 2010;
-- SELECT title, released_year FROM books WHERE released_year BETWEEN 2004 AND 2014;
-- SELECT title, author_lname FROM books WHERE author_lname IN ('Carver', 'Lahiri', 'Smith');

-- SELECT 
--     title,
--     stock_quantity,
--     CASE
--         WHEN stock_quantity <= 40 THEN '*'
--         WHEN stock_quantity <= 70 THEN '**'
--         WHEN stock_quantity <= 100 THEN '***'
--         WHEN stock_quantity <= 140 THEN '****'
--         ELSE '*****'
--     END AS stock
-- FROM
--     books;

-- CREATE TABLE customers (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     email VARCHAR(50)
-- );
--  
-- CREATE TABLE orders (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     order_date DATE,
--     amount DECIMAL(8 , 2 ),
--     customer_id INT,
--     FOREIGN KEY (customer_id)
--         REFERENCES customers (id)
--         ON DELETE CASCADE
-- );
CREATE TABLE reviewers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);
 
CREATE TABLE series (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    released_year YEAR,
    genre VARCHAR(100)
);
 
CREATE TABLE reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    rating DECIMAL(2 , 1 ),
    series_id INT,
    reviewer_id INT,
    FOREIGN KEY (series_id)
        REFERENCES series (id),
    FOREIGN KEY (reviewer_id)
        REFERENCES reviewers (id)
);
 
INSERT INTO series (title, released_year, genre) VALUES
    ('Archer', 2009, 'Animation'),
    ('Arrested Development', 2003, 'Comedy'),
    ("Bob's Burgers", 2011, 'Animation'),
    ('Bojack Horseman', 2014, 'Animation'),
    ("Breaking Bad", 2008, 'Drama'),
    ('Curb Your Enthusiasm', 2000, 'Comedy'),
    ("Fargo", 2014, 'Drama'),
    ('Freaks and Geeks', 1999, 'Comedy'),
    ('General Hospital', 1963, 'Drama'),
    ('Halt and Catch Fire', 2014, 'Drama'),
    ('Malcolm In The Middle', 2000, 'Comedy'),
    ('Pushing Daisies', 2007, 'Comedy'),
    ('Seinfeld', 1989, 'Comedy'),
    ('Stranger Things', 2016, 'Drama');
 
 
INSERT INTO reviewers (first_name, last_name) VALUES
    ('Thomas', 'Stoneman'),
    ('Wyatt', 'Skaggs'),
    ('Kimbra', 'Masters'),
    ('Domingo', 'Cortes'),
    ('Colt', 'Steele'),
    ('Pinkie', 'Petit'),
    ('Marlon', 'Crafford');
    
 
INSERT INTO reviews(series_id, reviewer_id, rating) VALUES
    (1,1,8.0),(1,2,7.5),(1,3,8.5),(1,4,7.7),(1,5,8.9),
    (2,1,8.1),(2,4,6.0),(2,3,8.0),(2,6,8.4),(2,5,9.9),
    (3,1,7.0),(3,6,7.5),(3,4,8.0),(3,3,7.1),(3,5,8.0),
    (4,1,7.5),(4,3,7.8),(4,4,8.3),(4,2,7.6),(4,5,8.5),
    (5,1,9.5),(5,3,9.0),(5,4,9.1),(5,2,9.3),(5,5,9.9),
    (6,2,6.5),(6,3,7.8),(6,4,8.8),(6,2,8.4),(6,5,9.1),
    (7,2,9.1),(7,5,9.7),
    (8,4,8.5),(8,2,7.8),(8,6,8.8),(8,5,9.3),
    (9,2,5.5),(9,3,6.8),(9,4,5.8),(9,6,4.3),(9,5,4.5),
    (10,5,9.9),
    (13,3,8.0),(13,4,7.2),
    (14,2,8.5),(14,3,8.9),(14,4,8.9);