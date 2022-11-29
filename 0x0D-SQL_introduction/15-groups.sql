-- returns number of records and 
-- score of the table attribute
SELECT score, COUNT('score') AS number FROM second_table GROUP BY score ORDER BY score DESC
