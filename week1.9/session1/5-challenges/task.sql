.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- Bronze
.schema drivers;
SELECT name, price FROM menu_items;
SELECT name FROM restaurants WHERE cuisine = 'Indian';

-- Silver
SELECT name, price FROM menu_items WHERE price <= 8 order by price asc;
SELECT name, hygiene_rating FROM restaurants WHERE hygiene_rating < 4 order by hygiene_rating desc;
SELECT name, postcode FROM restaurants WHERE postcode LIKE 'LS6%' order by hygiene_rating desc;