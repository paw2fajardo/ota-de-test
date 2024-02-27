import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import config.config as config

DATABASE = config.DATABASE
CREATE_TABLE_QUERY = config.CREATE_TABLE_QUERY
TABLE_NAME = config.TABLE_NAME
DATA = config.DATA
DAILY_TOTAL_AMOUNT_QUERY = config.DAILY_TOTAL_AMOUNT_QUERY


def _create_table_if_not_exist(db, query_path):
    """
    Create a table in the given database if it does not already exist using the
    SQL query specified in the provided query_path.

    Args:
        db (str): The path to the SQLite database.
        query_path (str): The path to the SQL query file.

    Returns:
        None
    """
    with open(query_path, 'r', encoding='utf-8') as f, \
            sqlite3.connect(db) as conn:
        create_query = f.read().replace('{TABLE_NAME}', TABLE_NAME)
        conn.execute(create_query)
        conn.commit()


def _append_data_to_table(db, table_name, df):
    """
    Append data to a table in the specified database using the provided
    DataFrame.

    Parameters:
    db (str): The path to the SQLite database.
    table_name (str): The name of the table to which the data will be appended.
    df (pd.DataFrame): The DataFrame containing the data to be appended.

    Returns:
    None
    """
    with sqlite3.connect(db) as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)


def _run_select_query(db, table_name, query_path):
    """
    Run a select query on the specified database using the provided SQL
    query file.

    Parameters:
    - db: the path to the database file
    - table_name: the name of the table to query
    - query_path: the path to the SQL query file

    Returns:
    - A pandas DataFrame containing the results of the SQL query
    """
    with open(query_path, 'r', encoding='utf-8') as f, \
            sqlite3.connect(db) as conn:
        sql_query = f.read().replace('{TABLE_NAME}', table_name)
        return pd.read_sql_query(sql_query, conn)


def _create_bar_chart(df, x, y, chart_title, legend=None):
    """
    Creates a bar chart using the provided DataFrame and specified
    x and y columns.

    Parameters:
    df (DataFrame): The input DataFrame.
    x (str): The column name for the x-axis.
    y (str): The column name for the y-axis.
    chart_title (str): The title of the bar chart.
    legend (bool, optional): Whether to display the legend. Defaults to None.
    """
    ax = df.plot(kind='bar', x=x, y=y, legend=legend)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(chart_title)
    for i, val in enumerate(df[y]):
        formatted_val = '{:,.2f}'.format(val)
        bar_height = ax.patches[i].get_height()
        ax.text(i, bar_height / 2, formatted_val,
                ha='center', va='center', rotation=90)
    plt.show()


def filter_dataframe(df, col, condition):
    """Filter the dataframe based on the provided column and condition.

    Parameters:
    - df (DataFrame): The dataframe to filter.
    - col (str): The column name based on which to filter.
    - condition (callable): A function that takes a column and returns a
    boolean array.

    Returns:
    - DataFrame: The filtered dataframe.
    """
    return df[condition(df[col])]


def main():
    print(f'Loading data from {DATA}')
    df = pd.read_parquet(DATA)
    print(f'Loaded {len(df)} rows')

    print('Filtering data')
    filtered_df = filter_dataframe(df, 'passenger_count', lambda x: x > 0)
    print(f'Filtered {len(filtered_df)} rows')

    print('Checking if table exists and creating table')
    _create_table_if_not_exist(db=DATABASE, query_path=CREATE_TABLE_QUERY)
    print(f'Created table {TABLE_NAME}')

    print('Appending data to table')
    _append_data_to_table(db=DATABASE, table_name=TABLE_NAME, df=filtered_df)
    print(f'Appended {len(filtered_df)} rows')

    print('Running daily total amount query')
    daily_total_amount = _run_select_query(db=DATABASE, table_name=TABLE_NAME,
                                           query_path=DAILY_TOTAL_AMOUNT_QUERY)
    print(f'Running query {DAILY_TOTAL_AMOUNT_QUERY}')

    print('Creating bar chart')
    _create_bar_chart(df=daily_total_amount, x='drop_off_date',
                      y='daily_total_amount',
                      chart_title='Daily Amount by Drop Off Date')
    print(f'Created bar chart Daily Amount by Drop Off Date')


if __name__ == '__main__':
    main()
