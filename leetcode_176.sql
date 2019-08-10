-- 176. Second Highest Salary

SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary NOT IN(
    SELECT MAX(Salary)
    FROM Employee )