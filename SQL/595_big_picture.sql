/*
Solution 1 (Most Intuitive)
Intuition and Approach
- Use the SELECT and FROM key words to retrieve the name, area and population columns from World table
- Use WHERE to check of "big" country conditions
*/

SELECT name, area, population
FROM World
WHERE area >= 3000000 OR population >= 25000000;
