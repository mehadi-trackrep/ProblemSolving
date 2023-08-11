/*
    Write a query to print the 
    
    contest_id, 
    hacker_id, 
    name, and 
    the sums of total_submissions, 
    total_accepted_submissions, 
    total_views, and 
    total_unique_views 
    
    for each contest sorted by contest_id. 
    
    Exclude the contest from the result if all four sums are .

V.V.I. -- this PROBLEM MYSQL SQL Engine doesn't support CTE! :(
    But in MYSQL Server! it works fine! :)

*/

/*

Soultion 1: Using CTE

*/

SELECT 
   con.contest_id
  ,con.hacker_id
  ,con.name
  ,SUM(ts)
  ,SUM(tas)
  ,SUM(tv)
  ,SUM(tuv)
FROM 
  contests con 
  INNER JOIN colleges col ON (con.contest_id = col.contest_id)
  INNER JOIN challenges cha ON (col.college_id = cha.college_id)
  LEFT JOIN (
      SELECT 
         Challenge_id
        ,SUM(total_views) tv
        ,SUM(total_unique_views) tuv
      FROM 
        view_stats 
      GROUP BY
        1
  )vv ON (cha.challenge_id = vv.challenge_id)
  LEFT JOIN (
      SELECT 
         Challenge_id
        ,SUM(total_submissions) ts
        ,SUM(total_accepted_submissions) tas
      FROM 
        Submission_Stats 
      GROUP BY
        1
  )ss ON (cha.challenge_id = ss.challenge_id)
GROUP BY
   1 
  ,2
  ,3
HAVING 
  SUM(ts) + SUM(tas) + SUM(tv) + SUM(tuv) > 0 -- V.V.I. => https://shorturl.at/rFRW7
ORDER BY
  1;

/*

Testing with the input data without creating any table in MYSQL Server physically!

*/

WITH 
Challenges AS (

    SELECT 18765 AS challenge_id, 11219 AS college_id
    UNION ALL
    SELECT 47127 AS challenge_id, 11219 AS college_id
    UNION ALL
    SELECT 60292 AS challenge_id, 32473 AS college_id
    UNION ALL
    SELECT 72974 AS challenge_id, 56685 AS college_id
)

, View_Stats AS (
    
    SELECT 47127 AS challenge_id, 26 AS total_views, 19 AS total_unique_views
    UNION ALL
    SELECT 47127 AS challenge_id, 15 AS total_views, 14 AS total_unique_views
    UNION ALL
    SELECT 18765 AS challenge_id, 43 AS total_views, 10 AS total_unique_views
    UNION ALL
    SELECT 18765 AS challenge_id, 72 AS total_views, 13 AS total_unique_views
    UNION ALL
    SELECT 75516 AS challenge_id, 35 AS total_views, 17 AS total_unique_views
    UNION ALL
    SELECT 60292 AS challenge_id, 11 AS total_views, 10 AS total_unique_views
    UNION ALL
    SELECT 72974 AS challenge_id, 41 AS total_views, 15 AS total_unique_views
    UNION ALL
    SELECT 75516 AS challenge_id, 75 AS total_views, 11 AS total_unique_views
)

, Submission_Stats AS (
    
    SELECT 75516 AS challenge_id, 34 AS total_submissions, 12 AS total_accepted_submissions
    UNION ALL
    SELECT 47127 AS challenge_id, 27 AS total_submissions, 10 AS total_accepted_submissions
    UNION ALL
    SELECT 47127 AS challenge_id, 56 AS total_submissions, 18 AS total_accepted_submissions
    UNION ALL
    SELECT 75516 AS challenge_id, 74 AS total_submissions, 12 AS total_accepted_submissions
    UNION ALL
    SELECT 75516 AS challenge_id, 83 AS total_submissions, 8 AS total_accepted_submissions
    UNION ALL
    SELECT 72974 AS challenge_id, 68 AS total_submissions, 24 AS total_accepted_submissions
    UNION ALL
    SELECT 72974 AS challenge_id, 82 AS total_submissions, 14 AS total_accepted_submissions
    UNION ALL
    SELECT 47127 AS challenge_id, 28 AS total_submissions, 11 AS total_accepted_submissions
),

sum_of_submissions AS(
    SELECT
         cha.college_id AS college_id
        ,SUM(sus.total_submissions) AS sum_of_total_submissions
        ,SUM(sus.total_accepted_submissions) AS sum_of_total_accepted_submissions
    FROM
        Challenges cha
        JOIN Submission_Stats sus ON(cha.challenge_id=sus.challenge_id)
    GROUP BY
        1
),

sum_of_views AS(
    SELECT
         cha.college_id AS college_id
        ,SUM(vis.total_views) AS sum_of_total_views
        ,SUM(vis.total_unique_views) AS sum_of_total_unique_views
    FROM
        Challenges cha
        JOIN View_Stats vis ON(cha.challenge_id=vis.challenge_id)
    GROUP BY
        1
)


SELECT
    CASE
        WHEN sos.college_id IS NOT NULL THEN sos.college_id
        ELSE sov.college_id
    END AS college_id,
    CASE
        WHEN sos.sum_of_total_submissions IS NOT NULL THEN sos.sum_of_total_submissions
        ELSE 0
    END AS sum_of_total_submissions,
    CASE
        WHEN sos.sum_of_total_accepted_submissions IS NOT NULL THEN sos.sum_of_total_accepted_submissions
        ELSE 0
    END AS sum_of_total_accepted_submissions,
    CASE
        WHEN sov.sum_of_total_views IS NOT NULL THEN sov.sum_of_total_views
        ELSE 0
    END AS sum_of_total_views,
    CASE
        WHEN sov.sum_of_total_unique_views IS NOT NULL THEN sov.sum_of_total_unique_views
        ELSE 0
    END AS sum_of_total_unique_views
FROM sum_of_submissions sos FULL JOIN sum_of_views sov ON (sos.college_id=sov.college_id)