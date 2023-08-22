
/*
    In the Employee table, the salary is the per month salary
    So, if an employee have months=10 & salary=2000, then his/her
    total earnings is 2000*10 = 20000

    V.V.I. and, we can use any column name in the ORDER BY clause 
                even though the column name is not present in the SELECT clause
*/



SELECT NAME
FROM EMPLOYEE
WHERE SALARY > 2000 AND MONTHS < 10
ORDER BY EMPLOYEE_ID

/*
    Good approach to write a query:-
*/

SELECT
    name
FROM
    Employee
WHERE
    months<10
        and
    salary > 2000
ORDER BY
    employee_id