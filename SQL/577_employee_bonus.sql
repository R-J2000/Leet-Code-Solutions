# 577 Employee Bonus

/*
Solution 1 (Most Intuitive)
Intuition and Approach
- Use the SELECT and FROM key words to retrieve the name and bonus fields from their respective tables
- RIGHT JOIN the two table for rows where Employee.empID = Bonus.empID is satisfied and ALL rows of the name column are preserved.
- Use a WHERE clause to disregard any bonus values higher than 1000.
*/

SELECT Employee.name, Bonus.bonus
FROM Bonus
RIGHT JOIN Employee ON Employee.empID = Bonus.empID
WHERE IFNULL(Bonus.bonus, 0) < 1000
