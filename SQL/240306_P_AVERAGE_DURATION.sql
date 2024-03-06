-- 확인
SELECT *
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY

-- datediff 함수로 대여 기간
-- '+1' 해줘야 하루 빌린 것도 계산
SELECT *
      , datediff(end_date, start_date)+1 as DAYS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY

-- ROUND(숫자, 소수자리)
SELECT a.CAR_ID
        , ROUND(AVG(a.DAYS),1) as AVERAGE_DURATION
    FROM (SELECT *
                  , datediff(end_date, start_date)+1 as DAYS
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) as a
    GROUP BY CAR_ID
    HAVING AVERAGE_DURATION >= 7
    ORDER BY AVERAGE_DURATION desc, CAR_ID desc;