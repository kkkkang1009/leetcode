-- 181. Employees Earning More Than Their Managers

SELECT A.Name AS Employee
FROM EMPLOYEE A
LEFT JOIN EMPLOYEE B
ON A.ManagerID = B.Id
WHERE A.Salary > B.Salary