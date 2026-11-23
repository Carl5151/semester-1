.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- Bronze
-- .schema drivers;
-- SELECT name, price FROM menu_items;
-- SELECT name FROM restaurants WHERE cuisine = 'Indian';

-- Silver
-- SELECT name, price FROM menu_items WHERE price <= 8 ORDER BY price ASC;
-- SELECT name, hygiene_rating FROM restaurants WHERE hygiene_rating < 4 ORDER BY hygiene_rating DESC;
-- SELECT name, postcode FROM restaurants WHERE postcode LIKE 'LS6%' ORDER BY hygiene_rating DESC;
-- SELECT email FROM customers WHERE email LIKE '%@leeds.ac.uk' ORDER BY joined_date DESC;
-- SELECT * FROM orders WHERE status = 'cancelled' ORDER BY order_time DESC LIMIT 10;
SELECT name FROM menu_items WHERE restaurant_id = 4 AND is_vegetarian = 1;
SELECT name, price FROM menu_items WHERE restaurant_id = 4 ORDER BY price DESC LIMIT 1;