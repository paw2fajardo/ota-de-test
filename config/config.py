import os

BASE_PATH = os.path.abspath(os.curdir)
DATABASE = os.path.join(BASE_PATH, 'sql', 'data.db')
CREATE_TABLE_QUERY = os.path.join(BASE_PATH, 'queries', 'create_table.sql')
DAILY_TOTAL_AMOUNT_QUERY = os.path.join(BASE_PATH, 'queries', 'daily_total_amount.sql')
TABLE_NAME = 'trip_records'
DATA = os.path.join(BASE_PATH, 'files', 'yellow_tripdata_2023-01.parquet')
