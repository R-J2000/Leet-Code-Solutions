# 584: Find Customer Referee
/* 
Solution 1 (Most Intuitive)
  
Intuition and Approach
- Use the SELECT and FROM key words to retrieve the name column from Customers table
- Use the WHERE to filter rows, ensuring only those rows are displayed where the specified conditions (id is not 2) are met.

Special Notes:
- We need to include the IS NULL condition since the database treats NULL values as missing and with MySQL we need to explicitly 
  state that we want ALSO want names corresponding to NULL values.
*/

SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;

/*
Solution 2 (using COALESCE)
Intuition and Approach
- Use the SELECT and FROM key words to retrieve the name column from Customers table
- Use WHERE, with the COALESCE key word to filter rows. COALESCE returns the first non-NULL character in a list of expressions. (The list in this case being (referee_id,0)) If referee_id is NOT NULL it will return referee_id and check if it != 2. If referee_id is NULL, it will select 0 and check to see if it != 2.
- The overall effect of this approach is that only rows where referee_id = 2 will be filtered. 

Special Notes
- I find this approach distasteful. It isn't particularly intuitive and neither better in terms of efficency.
  Though it is valuable to know the COALESCE key word as it often comes handy when dealing with NULL values.
-Fun Fact: It is called COALESCE because it resembles a Many-to-One mapping. The Many refers to the list of 
  expressions presented in the argument. The One is the first non-NULL value returned.
*/
  
SELECT name
FROM Customer
WHERE COALESCE(referee_id, 0) != 2;

/*
Solution 3 (Using IFNULL: THE BEST!)
Intuition and Approach
- Use the SELECT and FROM key words to retrieve the name column from Customers table
- Use WHERE, with the IFNULL key word to filter rows. IFNULL referee_id if it is NOT NULL, checking if it != 2. If referee_id is NULL, it will select 0 and checks to see if it != 2.
- In other words, IFNULL checks if the first expression is NULL and if is it it returns the alernate expression: IFNULL(expression, alt_value)
*/
SELECT name
FROM Customer
WHERE IFNULL(referee_id,0) != 2;
