/*

When we will have 
    - same age & same power then we have to take only the minimum one!


*/
    
    
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
