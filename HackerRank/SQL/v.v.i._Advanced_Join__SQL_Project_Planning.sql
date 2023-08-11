/*
    Main hacks:-
        For each project we will have a Start_Date & End_Date
            where the Start_Date is unique in Start_Date column & doesn't exist in End_Date column
                and the End_Date is unique in End_Date column & doesn't exist in End_Date column.
    This is the rule or basis in this problem.
*/

WITH start_dates_of_all_projects AS(
    SELECT
        Start_Date
        ,ROW_NUMBER() OVER(ORDER BY Start_Date) as rn
    FROM
        Projects
    WHERE
        Start_Date NOT IN (
            SELECT End_Date FROM Projects
        )
),
end_dates_of_all_projects AS(
    SELECT
        End_Date
        ,ROW_NUMBER() OVER(ORDER BY End_Date) as rn
    FROM
        Projects
    WHERE
        End_Date NOT IN (
            SELECT Start_Date FROM Projects
        )
)

SELECT
    sd.Start_Date
    ,ed.End_Date
FROM
    start_dates_of_all_projects sd, end_dates_of_all_projects ed-- cartesian join OR:-
    -- start_dates_of_all_projects sd JOIN end_dates_of_all_projects ed ON(1=1)-- cartesian join
WHERE
    sd.rn=ed.rn
ORDER BY
    -- DATEDIFF(ed.End_Date,sd.Start_Date)
    (ed.End_Date - sd.Start_Date)
    ,sd.Start_Date