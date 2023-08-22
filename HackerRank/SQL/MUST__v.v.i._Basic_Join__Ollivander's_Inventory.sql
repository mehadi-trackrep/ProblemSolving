/*

When we will have 
    - same age & same power then we have to take only the minimum one!

Approach - 1: Using IN subquery
Approach - 2: Using JOIN subquery
*/
    
-- ## Approach - 1: Using IN subquery
SELECT 
  w.id, 
  p.age, 
  w.coins_needed, 
  w.power 
FROM 
  wands AS w 
  INNER JOIN wands_property AS p ON w.code = p.code 
WHERE 
  p.is_evil = 0 
  AND (w.power, w.code, w.coins_needed) IN (
    SELECT 
      power, 
      code, 
      min(coins_needed) 
    FROM 
      wands 
    GROUP BY 
      1, 
      2
  ) 
ORDER BY 
  4 DESC, 
  2 DESC;

-- ## Approach - 2: Using JOIN subquery


SELECT
     w.id
    ,wp.age
    ,pre_result.min_coins_needed
    ,pre_result.power
FROM
    wands w
    JOIN (
        SELECT
             w.code
            ,w.power
            ,MIN(w.coins_needed) AS min_coins_needed
        FROM
            wands w
            JOIN wands_property wp
                ON(w.code=wp.code)
        WHERE
            wp.is_evil=0
        GROUP BY
             1
            ,2
    )pre_result
        ON(w.code=pre_result.code AND w.power=pre_result.power AND w.coins_needed=pre_result.min_coins_needed)
    JOIN wands_property wp
        ON(pre_result.code=wp.code)
ORDER BY
     4 DESC
    ,2 DESC
;