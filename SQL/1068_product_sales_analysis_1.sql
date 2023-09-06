# 1068 Product Sales Analysis I

/*
Solution (RIGHT JOIN)

Intuition and Approach
- SELECT fields to be rendered. Since we are not dealing with primary key we 
need to guard against duplicate values
- RIGHT JOIN Sales onto Product where Sales.product_id = Product.product_id
Special Notes:
*/

SELECT DISTINCT Product.product_name, Sales.year, Sales.price
FROM Product
RIGHT JOIN Sales ON Sales.product_id = Product.product_id 
