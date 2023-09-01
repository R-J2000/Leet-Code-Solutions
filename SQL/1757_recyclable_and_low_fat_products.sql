# 1757: Recyclable and Low Fat Products
/*
Intuition and Approach
- Use the SELECT and FROM key words to retrieve the product_id column from Products Table
- Use the WHERE to filter rows, ensuring only those rows where the specified conditions are met (the product
    is both low fat and recyclable) remain in the retrieved column
*/

SELECT product_id 
FROM Products
WHERE low_fats='Y' AND recyclable='Y';
