.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

SELECT name FROM drivers;  -- 1
SELECT name FROM menu_items WHERE price > 10; -- 2
SELECT postcode FROM restaurants WHERE postcode LIKE 'LS2%'; -- 3
-- 4 - ORDER BY should be after the WHERE condition
-- 5 - degree is 3 since there are 3 attributes (columns)
