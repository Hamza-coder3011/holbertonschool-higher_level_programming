-- Lists all records in the table with non-empty name, ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
