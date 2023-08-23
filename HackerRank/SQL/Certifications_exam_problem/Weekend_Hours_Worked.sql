'''

    We have to find the toal working hours per
    employee on weekends (sat & sun).

'''


WITH
add_date_in_attendance AS(
    SELECT 
        timestamp, 
        emp_id, 
        LEFT(timestamp, 10) AS date
    FROM attendance    
),
total_hours_per_date_for_all_emp_ids AS(
    SELECT 
        emp_id
        ,date
        ,TIMESTAMPDIFF(HOUR, MIN(timestamp), MAX(timestamp)) AS total_hours
    FROM
        add_date_in_attendance
    WHERE
        WEEKDAY(date) IN (5,6)
    GROUP BY
        emp_id
        ,date
)

SELECT
     emp_id
    ,SUM(total_hours)
FROM
    total_hours_per_date_for_all_emp_ids
GROUP BY
    emp_id
;