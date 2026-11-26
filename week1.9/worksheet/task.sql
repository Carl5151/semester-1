.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries


-- degree & cardinality of table stations
-- .schema stations
-- SELECT COUNT(*) as Cardinality FROM stations;


-- number of total relations in the aire_bikes database
-- .tables


-- capacity of Hyde Park Corner station
-- SELECT capacity FROM stations WHERE name = 'Hyde Park Corner'


-- when bike 5 was added to the scheme
-- SELECT year_added FROM bikes WHERE bike_id = '5'


-- amount of stations with capcity 16
-- SELECT * FROM stations WHERE capacity = 16

-- amount of stations with capcity greater than 16
-- SELECT * FROM stations WHERE capacity > 16


-- bikes from 2022
-- SELECT bike_id From bikes WHERE year_added LIKE '__22'


-- updating all trips under 5 minutes long to be free
-- UPDATE trips SET cost = 0 WHERE duration_mins < 5