SELECT 
DATE(tpep_dropoff_datetime) as drop_off_date,
SUM(total_amount) daily_total_amount
FROM {TABLE_NAME}
GROUP BY drop_off_date
HAVING drop_off_date BETWEEN '2023-01-01' AND '2023-01-31'
ORDER BY drop_off_date ASC