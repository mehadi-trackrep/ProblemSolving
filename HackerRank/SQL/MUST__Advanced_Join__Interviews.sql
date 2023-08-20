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

    Here, in the test case tables, after LEFT JOIN, there will be no NULL values that's why we
        didn't require any CASE WHEN clause. :)

*/

    V.V.I. ==> Blog link from Adil! - https://medium.com/@ikaadil007/486de13a018

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

Contests AS (

    SELECT 66406 AS contest_id, 17973 AS hacker_id, 'Rose' AS `name`
    UNION ALL
    SELECT 66556 AS contest_id, 79153 AS hacker_id, 'Angela' AS `name`
    UNION ALL
    SELECT 94828 AS contest_id, 80275 AS hacker_id, 'Frank' AS `name`
),

Colleges AS (

    SELECT 11219 AS college_id, 66406 AS contest_id
    UNION ALL
    SELECT 32473 AS college_id, 66556 AS contest_id
    UNION ALL
    SELECT 56685 AS college_id, 94828 AS contest_id
),

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

challenge_id_wise_sum_of_Submission_Stats AS ( -- means in this CTE, we will have no duplicate rows for each challenge_id, so that when we will join to other table then it will not produce any duplicate rows and thereby we will get rid of summation of same values again and again.
    SELECT
         challenge_id
        ,SUM(total_submissions) AS sum_of_total_submissions
        ,SUM(total_accepted_submissions) AS sum_of_total_accepted_submissions
    FROM
        Submission_Stats
    GROUP BY
        challenge_id
),

challenge_id_wise_View_Stats AS (
    SELECT
         challenge_id
        ,SUM(total_views) AS sum_of_total_views
        ,SUM(total_unique_views) AS sum_of_total_unique_views
    FROM
        View_Stats
    GROUP BY
        challenge_id
)

SELECT
     con.contest_id
    ,con.hacker_id
    ,con.name
    ,SUM(sub.sum_of_total_submissions)
    ,SUM(sub.sum_of_total_accepted_submissions)
    ,SUM(vie.sum_of_total_views)
    ,SUM(vie.sum_of_total_unique_views)
FROM 
  Contests con 
  JOIN Colleges col 
      ON (con.contest_id=col.contest_id)
  JOIN Challenges cha 
      ON(col.college_id=cha.college_id)
  LEFT JOIN challenge_id_wise_sum_of_Submission_Stats sub 
      ON(cha.challenge_id=sub.challenge_id)
  LEFT JOIN challenge_id_wise_View_Stats vie 
      ON(cha.challenge_id=vie.challenge_id)
GROUP BY
     con.contest_id
    ,con.hacker_id
    ,con.name
HAVING
     SUM(sub.sum_of_total_submissions)
    +SUM(sub.sum_of_total_accepted_submissions)
    +SUM(vie.sum_of_total_views)
    +SUM(vie.sum_of_total_unique_views)
    > 0
ORDER BY
    con.contest_id
;
