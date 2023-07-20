-- ## here, we have only two points, so, result will be a decimal value
-- ## P1(a, c), P2(b,d) so, sqrt((a-b)^2 + (c-d)^2)

SELECT  ROUND(
            SQRT(
                POWER((MIN(LAT_N) - MAX(LAT_N)), 2) 
                    + 
                POWER((MIN(LONG_W) - MAX(LONG_W)), 2)
            ), 4
        )
FROM STATION;