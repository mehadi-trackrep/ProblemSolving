

/*

We will use recursive CTE as a loop in MySQL.
Here, we will have two conditions:-
    1) initial row values
    2) terminating condition
In this example, we have to start from 20 (this is the initial row value),
and the recursion will go upto 1 (this is the terminating condition).
Here, we have a single column.

SYNTAX:

WITH RECURSIVE CTE_name(column_name) AS(
    SELECT initial_value
        UNION ALL
    SELECT column_name-1 FROM CTE_name WHERE column_name>terminating_condition
)

*/

WITH RECURSIVE P(R) AS(
    SELECT 20
        UNION ALL
    SELECT R-1 FROM P WHERE R>1
)
SELECT REPEAT('* ', R) FROM P;
-- SELECT CONCAT(REPEAT('* ', R-1), '*') FROM P; -- OR