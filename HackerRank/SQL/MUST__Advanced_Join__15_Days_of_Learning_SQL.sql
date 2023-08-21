WITH

hackers_who_exist_each_day AS( -- V.V.I. here the magic happens!! complex logic about dates
                -- suppose, we are finding the hackers who submitted on 2016-03-04, so the 
                -- hackers will be valid if they submitted on 2016-03-01, 2016-03-02, 2016-03-03 & 2016-03-04
  SELECT 
      submission_date
      ,hacker_id
  FROM 
    Submissions sub1 
  WHERE 
    hacker_id IN (
        SELECT 
            hacker_id
        FROM 
            Submissions sub2
        WHERE 
            sub2.submission_date <= sub1.submission_date
        GROUP BY 
            hacker_id
        HAVING 
            COUNT(DISTINCT sub2.submission_date) = DATEDIFF(day, '2016-03-01', sub1.submission_date) + 1
  )
 ),
count_unique_hackers_per_day AS( -- result_part1
    SELECT
         submission_date
        ,COUNT(DISTINCT hacker_id) AS total_unique_hackers
    FROM
        hackers_who_exist_each_day
    GROUP BY
        submission_date
),
max_submitted_hackers_in_a_day AS( -- last part result
    SELECT
         submission_date
        ,hacker_id
        ,COUNT(submission_id) AS total_submissions
    FROM
        Submissions
    GROUP BY
         submission_date
        ,hacker_id
),
only_max_submitted_hacker_per_day AS(
    SELECT
        submission_date
        ,hacker_id
        ,total_submissions
        ,ROW_NUMBER() OVER(PARTITION BY submission_date ORDER BY submission_date,total_submissions DESC,hacker_id) AS rn
    FROM
        max_submitted_hackers_in_a_day
),
result_part2 AS( -- result_part2
  SELECT
       submission_date
      ,hacker_id
      ,total_submissions
  FROM
      only_max_submitted_hacker_per_day
  WHERE
      rn=1
)

SELECT -- merge result_part2 with result_part1 (count_unique_hackers_per_day) and Hackers table
     rp2.submission_date
    ,cuhpd.total_unique_hackers
    ,rp2.hacker_id
    ,h.name
FROM
    count_unique_hackers_per_day AS cuhpd
    JOIN result_part2 AS rp2
        ON(cuhpd.submission_date=rp2.submission_date)
    JOIN Hackers AS h
        ON(rp2.hacker_id=h.hacker_id)

-- select * from result_part2
-- select * from hackers_who_exist_each_day
-- select * from count_unique_hackers_per_day

-- N.B. We can do a single CTE for hackers_who_exist_each_day & count_unique_hackers_per_day :-
/*

count_unique_hackers_per_day AS(
  SELECT 
      submission_date
      ,COUNT(distinct hacker_id) AS total_unique_hackers
  FROM 
    Submissions sub1 
  WHERE 
    hacker_id IN (
        SELECT 
            hacker_id
        FROM 
            Submissions sub2
        WHERE 
            sub2.submission_date <= sub1.submission_date
        GROUP BY 
            hacker_id
        HAVING 
            COUNT(DISTINCT sub2.submission_date) = DATEDIFF(day, '2016-03-01', sub1.submission_date) + 1
  )
  GROUP BY
      submission_date
)

*/

;
 