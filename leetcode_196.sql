-- 196. Delete Duplicate Emails
-- SELECT min(Id), Email
-- FROM Person
-- GROUP BY Email

DELETE FROM Person
WHERE Id NOT IN
(SELECT Id FROM
 (SELECT min(Id) Id
  FROM Person
  GROUP BY Email) p)