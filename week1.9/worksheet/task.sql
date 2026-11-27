.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- degree & cardinality of table stations
SELECT COUNT(*) as Cardinality FROM stations;

-- degree, amount of attributes in table members
.schema members;

-- number of total relations in the aire_bikes database
.tables;

-- capacity of Royal Armouries station
SELECT capacity FROM stations WHERE name = 'Royal Armouries';

-- when bike 5 was added to the scheme
SELECT year_added FROM bikes WHERE bike_id = '5';

-- amount of stations with capcity 16
SELECT * FROM stations WHERE capacity = 16;

-- amount of stations with capcity greater than 16
SELECT * FROM stations WHERE capacity > 16;

-- stations that end in Road
SELECT name From stations WHERE name LIKE '%Road';
