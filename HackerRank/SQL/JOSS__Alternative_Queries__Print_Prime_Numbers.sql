/*
    APPROACH 1: taking only the prime numbers in filter clause
*/

WITH RECURSIVE all_numbers AS (
    SELECT 2 AS num
        UNION
    SELECT num + 1 FROM all_numbers WHERE num <= 1000
)

SELECT GROUP_CONCAT(num SEPARATOR '&')
FROM all_numbers an1
WHERE (
    SELECT COUNT(*)
    FROM all_numbers an2
    WHERE an1.num % an2.num = 0
) = 1

/*
    APPROACH 2: filter outing the non-prime numbers in filter clause
*/

WITH RECURSIVE all_numbers AS (
    SELECT 2 AS num
        UNION
    SELECT num + 1 FROM all_numbers WHERE num <= 1000
)

SELECT GROUP_CONCAT(num SEPARATOR '&')
FROM all_numbers an1
WHERE NOT EXISTS( -- 'Correlated Subquery' is being used here where each subquery is executed once for every row of the outer query.
                        -- here, outer query table: an1 & subquery table: an2 [row-by-row processing/comparing]
    SELECT num
    FROM all_numbers an2
    WHERE an1.num % an2.num = 0
        AND an1.num != an2.num
)