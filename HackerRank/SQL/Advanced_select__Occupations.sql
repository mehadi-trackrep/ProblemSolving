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

-- We have two solutions so far!! --> 

-- 1. Using CTE per OCCUPATION & solution (2) is it's optimised version using PARTITION BY!

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


-- 2. Using PARTITION BY per OCCUPATION
WITH FOUR_COLUMNS_WITH_ROW_NUMBER AS (
    SELECT
        CASE WHEN OCCUPATION = 'Doctor' THEN Name ELSE NULL END Doctor,
        CASE WHEN OCCUPATION = 'Professor' THEN Name ELSE NULL END Professor,
        CASE WHEN OCCUPATION = 'Singer' THEN Name ELSE NULL END Singer,
        CASE WHEN OCCUPATION = 'Actor' THEN Name ELSE NULL END Actor,

        ROW_NUMBER() OVER(PARTITION BY OCCUPATION ORDER BY NAME) RNUM
    FROM OCCUPATIONS
)

SELECT 
     MAX(Doctor), -- MAX() function is used in string column for getting the last name after alphabetically sorting!
     MAX(Professor),
     MAX(Singer),
     MAX(Actor)
FROM FOUR_COLUMNS_WITH_ROW_NUMBER
GROUP BY RNUM
-- HAVING RNUM=5
ORDER BY RNUM;

/*
SELECT * FROM FOUR_COLUMNS_WITH_ROW_NUMBER
output:-

NULL NULL NULL Eve 1
NULL NULL NULL Jennifer 2
NULL NULL NULL Ketty 3
NULL NULL NULL Samantha 4
Aamina NULL NULL NULL 1
Julia NULL NULL NULL 2
Priya NULL NULL NULL 3
NULL Ashley NULL NULL 1
NULL Belvet NULL NULL 2
NULL Britney NULL NULL 3
NULL Maria NULL NULL 4
NULL Meera NULL NULL 5
NULL Naomi NULL NULL 6
NULL Priyanka NULL NULL 7
NULL NULL Christeen NULL 1
NULL NULL Jane NULL 2
NULL NULL Jenny NULL 3
NULL NULL Kristeen NULL 4


*/
