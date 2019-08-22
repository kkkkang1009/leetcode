-- 182. Duplicate Emails

SELECT Email
FROM Person
GROUP BY Email
HAVING count(Email) > 1