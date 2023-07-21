/*

We have a thumb rule -  (V.V.I.)
    In the result(output table), 
        1. if we would like to add more columns then 
                we have to do JOIN operations (to make more wider)
        2. or if we would like to add more rows then 
                we have to do UNION operations (to make more taller/longer)

*/


/*
        Approach:-
        ----------
        Here, we have to make the output table wider, 
            so, we have to do JOIN operations
        But we have no common column to join, 
            so, we have to create a common column by using ROW_NUMBER() function.
*/


WITH DOCTOR AS (
    SELECT  
            NAME,
            ROW_NUMBER() OVER(ORDER BY NAME) AS RN
    FROM    OCCUPATIONS 
    WHERE   OCCUPATION='DOCTOR'
),
PROFESSOR AS(
    SELECT  
            NAME,
            ROW_NUMBER() OVER(ORDER BY NAME) AS RN
    FROM    OCCUPATIONS 
    WHERE   OCCUPATION='PROFESSOR'
),
SINGER AS (
    SELECT  
            NAME,
            ROW_NUMBER() OVER(ORDER BY NAME) AS RN
    FROM    OCCUPATIONS 
    WHERE   OCCUPATION='SINGER'
),
ACTOR AS (
    SELECT  
            NAME,
            ROW_NUMBER() OVER(ORDER BY NAME) AS RN
    FROM    OCCUPATIONS 
    WHERE   OCCUPATION='ACTOR'
)


SELECT
        D.NAME,
        P.NAME,
        S.NAME,
        A.NAME
FROM 
    PROFESSOR P  -- AS PROFESSOR table has total rows greater than others table so, we have to kept it left in the left join, and all other tables will be left join with this table (PROFESSOR)
    LEFT JOIN DOCTOR D
        ON P.RN=D.RN
    LEFT JOIN SINGER S
        ON P.RN=S.RN
    LEFT JOIN ACTOR A
        ON P.RN=A.RN;

