-- List score and name for rows where name IS NOT NULL ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
