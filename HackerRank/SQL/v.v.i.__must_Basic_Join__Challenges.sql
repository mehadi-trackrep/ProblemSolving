
/*
    Approach 1:-
        ** Ashfak bhai's code:-
*/

WITH challenge_count_cte AS (
  SELECT 
    hacker_id, 
    COUNT(distinct challenge_id) AS challenge_count 
  FROM 
    Challenges 
  GROUP BY 
    1
),

max_challenge_count_cte AS (
  SELECT 
    MAX(challenge_count) AS max_challenge_count 
  FROM 
    challenge_count_cte
),

hacker_count AS (
  SELECT 
    challenge_count, 
    COUNT(distinct hacker_id) AS cnt 
  FROM 
    challenge_count_cte a 
    JOIN max_challenge_count_cte b ON (1 = 1) -- (1=1) means we will take all rows , it's kinda of UNION ALL
  WHERE 
    challenge_count < max_challenge_count 
  GROUP BY 
    1 
  HAVING 
    COUNT(DISTINCT hacker_id) >= 2
), 

pre_result AS (
  SELECT 
    a.* 
  FROM 
    challenge_count_cte a 
    LEFT JOIN hacker_count b ON (
      a.challenge_count = b.challenge_count
    ) 
  WHERE 
    b.challenge_count IS null
) 

SELECT 
  a.hacker_id, 
  b.name, 
  a.challenge_count 
FROM 
  pre_result a 
  JOIN Hackers b ON (a.hacker_id = b.hacker_id) 
ORDER BY 
  3 DESC, 
  1


/*
    Approach 2:-
        ** My code:-
*/
WITH total_challenges_per_hacker_cte AS (
    SELECT 
        c.hacker_id AS hacker_id, 
        h.name AS name, 
        COUNT(c.challenge_id) AS total_challenges
    FROM 
        challenges c JOIN hackers h 
            ON c.hacker_id=h.hacker_id
    GROUP BY 1, 2
    -- ORDER BY 3 DESC, 1  -- এটা দিলে আসলে দরকার নাই এখানে! কিন্তু না দিলে WA দেই! Mysql Engine এ সমস্যা মনে হচ্ছে! 
),

total_occurrances_of_each_challenges_count_cte AS (
    SELECT 
        total_challenges, 
        COUNT(total_challenges) AS total_occurrances_of_each_challenges_count
    FROM 
        total_challenges_per_hacker_cte c
    GROUP BY 1
)
        
SELECT
    hacker_id, 
    name, 
    total_challenges
FROM total_challenges_per_hacker_cte
WHERE total_challenges IN (
        SELECT 
            total_challenges 
        FROM 
            total_occurrances_of_each_challenges_count_cte
        WHERE 
            total_occurrances_of_each_challenges_count=1
            OR
            total_challenges=( -- including the max number of challenges submitted hackers!
                SELECT 
                    total_challenges 
                FROM 
                    total_occurrances_of_each_challenges_count_cte
                ORDER BY total_challenges DESC
                LIMIT 1
            )
)
ORDER BY 3 DESC, 1
;
