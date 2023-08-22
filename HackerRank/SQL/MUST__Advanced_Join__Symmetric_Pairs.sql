
/*
    Solution - 1:
*/
WITH pre_result AS (
    SELECT
        f1.X AS X1
        ,f1.Y AS Y1
    FROM 
        functions f1 JOIN functions f2
            ON (f1.X=f2.Y AND f1.Y=f2.X)
),

result AS (
    SELECT
        X1
        ,Y1
        ,row_number() over(partition by X1, Y1) AS rn
    FROM
        pre_result
)

SELECT 
    X1
    ,Y1
FROM 
    result 
WHERE 
    rn=2 -- # it's for where X==Y, so if this row exist once in the table then this will not be in the output, so, when rn>1 then the (x,y) pair exist in different rows, and here count might be 2 or 3 or more, we have to show only one pair
    OR X1 < Y1 -- # here, rn=1 but we have to show only the pairs where X<Y.
ORDER BY
    X1

/*
    Solution - 2:
*/

SELECT 
  F1.X,
  F1.Y
FROM
  Functions AS F1
  JOIN Functions AS F2 
    ON (F1.X = F2.Y AND F2.X = F1.Y)
GROUP BY
  F1.X,
  F1.Y
HAVING
  COUNT(*) > 1 -- here, count(*)>1 means we will consider the row where x==y and that might have a symmetric pair in another row, so after self join the count of this row should be > 1 otherwise it will be excluded from output.
  OR F1.X < F1.Y -- this condition is for X<Y because in the problem statement actual condition is X<=Y means X==Y OR X<Y
ORDER BY
  F1.X;