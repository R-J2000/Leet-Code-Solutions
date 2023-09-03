# 1148 Article Views I

/*
Solution 1 (Most Intuitive)
Intuition and Approach
- Use the SELECT and DISTINCT key words to select all non-duplicate 'author_id's FROM the Views table. The outputted table is retitled to 'id'.
- Use WHERE key word to choose only does ids where author_id = viewer_id. 
- Use ORDER BY to order ids in ascending order
*/
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
