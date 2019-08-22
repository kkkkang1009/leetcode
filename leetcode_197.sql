-- 197. Rising Temperature
SELECT W1.Id
FROM Weather W1, Weather W2
WHERE W1.Temperature > W2.Temperature
AND W1.RecordDate = AddDate(W2.RecordDate, 1)