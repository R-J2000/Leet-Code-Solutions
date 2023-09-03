# 584: Find Customer Referee
/*
Solution 1 (Most Intuitive)
Intuition and Approach
- Use the SELECT and FROM key words to retrieve the name column from Customers table
- Use the WHERE to filter rows, ensuring only those rows are displayed where the specified conditions (id is not 2) are met.

Special Notes:
- We need to include the IS NULL condition since the database treats NULL values as missing and with MySQL we need to explicitly state that we want ALSO want names corresponding to NULL values.
*/

SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
