-- Script that will list all records of a table
-- Query  lists all records of the table second_table who have name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
