WITH
corresponding_month_for_each_date AS(
    SELECT
        record_date AS record_date,
        MONTH(record_date) AS month
    FROM
        temperature_records
),

max_value_from_the_6_months AS(
    SELECT
        c.month AS month,
        max(data_value) AS max
    FROM
        temperature_records t
        JOIN corresponding_month_for_each_date c
            ON(t.record_date=c.record_date)
    WHERE
        data_type='max'
    GROUP BY
        c.month
),
min_value_from_the_6_months AS(
    SELECT
        c.month AS month,
        min(data_value) AS min
    FROM
        temperature_records t
        JOIN corresponding_month_for_each_date c
            ON(t.record_date=c.record_date)
    WHERE
        data_type='min'
    GROUP BY
        c.month
),
avg_value_from_the_6_months AS(
    SELECT
        c.month AS month,
        CEILING(ROUND(AVG(data_value+0.0), 0)) AS avg
    FROM
        temperature_records t
        JOIN corresponding_month_for_each_date c
            ON(t.record_date=c.record_date)
    WHERE
        data_type='avg'
    GROUP BY
        c.month
)

SELECT
    mx.month,
    mx.max,
    mn.min,
    ag.avg
FROM 
    max_value_from_the_6_months mx
    JOIN min_value_from_the_6_months mn
        ON(mx.month=mn.month)
    JOIN avg_value_from_the_6_months ag
        ON(mn.month=ag.month)

;
