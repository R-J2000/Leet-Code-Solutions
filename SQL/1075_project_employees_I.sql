# 1075 Project Employees I

# SIMPLE SOLUITON

SELECT 
  project_id,
  ROUND(AVG(experience_years), 2) AS 'average_years'
FROM Employee 
INNER JOIN Project 
ON Employee.employee_id = Project.employee_id
GROUP BY Project.project_id;
