

/*
Enter your query here.
*/

SELECT T.TOTAL_EARNINGS, COUNT(T.EMPLOYEE_ID)
FROM EMPLOYEE E INNER JOIN
(
    SELECT EMPLOYEE_ID, MONTHS*SALARY AS TOTAL_EARNINGS
    FROM EMPLOYEE
) T
ON E.EMPLOYEE_ID=T.EMPLOYEE_ID
GROUP BY 1
ORDER BY 1 DESC
LIMIT 1;


