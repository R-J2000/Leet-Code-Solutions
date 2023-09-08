# 620 Not Boring Movies

/*
Solution 
Intuition and Approach
TOO OBVIOUS! 
*/

SELECT *
FROM Cinema
WHERE description != "boring" AND MOD(id, 2) = 1
ORDER BY rating DESC;
