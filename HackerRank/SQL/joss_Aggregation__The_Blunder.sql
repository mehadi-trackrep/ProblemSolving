
/*
    V.V.I. --> We don't need to use CAST / CONVERT functions!
*/

SELECT 
    
    CEIL(AVG(SALARY) - AVG(REPLACE(SALARY, '0', '')))
    -- OR, CEIL(AVG(SALARY) - AVG(CAST(REPLACE(CAST(SALARY AS CHAR), '0', '') AS DECIMAL)))
    
FROM EMPLOYEES
;   