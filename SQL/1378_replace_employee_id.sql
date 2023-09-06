# 1378 Replace Employee ID with the Unique Identifier
  
/*
Solution 1 (LEFT JOIN)

Intuition and Approach
- SELECT fields that to be fields/column to be rendered
- LEFT JOIN EmployeeUNI onto Employees where EmployeeUNI.id = Employees.id

Special Notes:
LEFT JOIN and RIGHT JOIN can be confusing. A good way to remember which the column that will return ALL the rows is the imagine 
that MySQL first JOINS the tables. Then, if the clause is a LEFT clause, the table left of the Join clause (or above) will retain 
all its rows. Conversly, if the clause is a RIGHT clause, the table right of the Join clause (or below) will retain all its rows.
*/

SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI ON EmployeeUNI.id = Employees.id


/*
Solution 2 (RIGHT JOIN)
  
Intuition and Approach
- SELECT fields that to be fields/column to be rendered
- RIGHT JOIN Employees onto EmployeeUNI where EmployeeUNI.id = Employees.id
*/
SELECT EmployeeUNI.unique_id, Employees.name
FROM EmployeeUNI
RIGHT JOIN Employees ON EmployeeUNI.id = Employees.id
