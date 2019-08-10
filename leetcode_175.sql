-- 175. Combine Two Tables

SELECT FirstName, LastName, City, State
From Person p
LEFT JOIN Address a
ON p.PersonId = a.PersonId