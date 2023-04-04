import sys
import pandas as pd
from typing import Dict, List, Union, Tuple, Any
from os import path
import mysql.connector as msql
from mysql.connector import Error
from sqlalchemy import create_engine, Engine, text
#import sqlalchemy as db
#import pymysql

import cred

XLSX_FILE = cred.XLSX_FILE

order_level: pd.DataFrame = pd.DataFrame(None)
order_line_items: pd.DataFrame = pd.DataFrame(None)

ORDER_LEVEL_COLUMNS = [
    'order_reference', 'first_name', 'last_name', 'company', 'address1',
    'address2', 'city', 'province_state', 'postal_zip', 'country',
    'phone_number', 'additional_info', 'preferred_shipping_service', 'status',
    'ship_complete'
]

ORDER_LINE_ITEMS_COLUMNS = [
    'order_reference', 'preferred_supplier', 'product_supplier_reference',
    'product_quantity', 'part_order_status', 'shipping_service',
    'tracking_number'
]

sql_mapping = {
    'Order Reference': 'order_reference',
    'Delivery First Name': 'first_name',
    'Delivery Last Name': 'last_name',
    'Delivery Company': 'company',
    'Delivery Address 1': 'address1',
    'Delivery Address 2': 'address2',
    'Delivery City': 'city',
    'Delivery State': 'province_state',
    'Delivery Post Code': 'postal_zip',
    'Delivery Country': 'country',
    'Delivery Phone': 'phone_number',
    'Delivery Notes': 'additional_info',
    'Preferred Shipping': 'preferred_shipping_service',
    'Status': 'status',
    'Ship Complete': 'ship_complete',
    'Preferred Supplier': 'preferred_supplier',
    'SKU': 'sku',
    'Product Supplier Reference': 'product_supplier_reference',
    'Product Quantity': 'product_quantity',
    'Part Order Status': 'part_order_status',
    'Shipping Service': 'shipping_service',
    'Tracking Number': 'tracking_number'
}


def xlsx_dataframe(filename: str) -> pd.DataFrame:
    """Given a filename, converts the excel file to a proper csv file.

    Args:
        filename (str): name of the excel file
    """
    # Basic error handling
    if ".xlsx" not in filename:
        print("Assuming xlsx extension")
        filename = filename + ".xlsx"
    if not path.isfile(filename):
        print("Invalid file")
        sys.exit()

    data = pd.read_excel(filename)
    data_frame = pd.DataFrame(data)
    # print(data_frame.head)
    return data_frame


def dataframe_cleanup(
        data_frame: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Clean up the dataframe and returns one with the required columns.

    Returns:
        pd.DataFrame: Two dataframes with the required
        columns, one for each table.
    """
    # Change column names to compatible sql names from the schema
    data_frame = data_frame.rename(columns=sql_mapping)

    # Drop all the unnecessary columns from the dataframe for order_level
    df1 = data_frame[data_frame.columns.intersection(ORDER_LEVEL_COLUMNS)]

    columns: List = df1.columns.values.tolist()
    print(columns)

    if (not all(columns)):
        print("Columns are not correct")
        sys.exit()

    # Drop all the unnecessary columns from the dataframe for order_level
    df2 = data_frame[data_frame.columns.intersection(
        ORDER_LINE_ITEMS_COLUMNS)]

    columns: List = df2.columns.values.tolist()
    print(columns)

    if (not all(columns)):
        print("Columns are not correct")
        sys.exit()

    return df1, df2


def msql_connect() -> Tuple[Any, Any]:
    """Connect to the database and returns the connection and cursor.

    Returns:
        Tuple[Any, Any]: Connection and cursor to the database
    """
    # conn = pymysql.connect(**kwargs)
    # try:
    #     yield conn
    # finally:
    #     conn.close()

    # database connection

    connection: Any = None
    cursor: Any = None

    try:
        connection = msql.connect(
            host=cred.DEFAULT_HOST,
            user=cred.DEFAULT_USER,
            password=cred.DEFAULT_PWD,
            port=cred.DEFAULT_PORT,
            database=cred.DATABASE_NAME)    # give ur username, password
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
    except Error as err:
        print("Error while connecting to MySQL", err)
        exit()

    return (connection, cursor)


def execute_queries(connection: Any, cursor: Any, query: str):
    """Execute the query on the database and prints the result.

    Args:
        connection (Any): Connection to the database
        cursor (Any): Cursor to the connection
        query (str): Query to be executed
    """
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor.execute(query)


def create_sql_engine() -> Engine:
    """Create a sql engine to connect to the database.

    Returns:
        Engine: Engine to connect to the database
    """
    creds = {
        'usr': cred.DEFAULT_USER,
        'pwd': cred.DEFAULT_PWD,
        'hst': cred.DEFAULT_HOST,
        'prt': cred.DEFAULT_PORT,
        'dbn': cred.DATABASE_NAME
    }
    connstr = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}'
    engine = create_engine(connstr.format(**creds))
    return engine


def insert_databases(order_level: pd.DataFrame,
                     order_line_items: pd.DataFrame,
                     sql_engine: Engine) -> None:
    """Insert the data into the database.
    
    Args:
        order_level (pd.DataFrame): Dataframe with the order_level data
        order_line_items (pd.DataFrame): Dataframe with the order_line_items data
    """
    order_level.to_sql(name='order_level',
                       con=sql_engine,
                       if_exists='append',
                       index=False)
    order_line_items.to_sql(name='order_line_items',
                            con=sql_engine,
                            if_exists='append',
                            index=False)


def query_table(engine: Engine) -> None:
    """Query the table and prints the result.

    Args:
        engine (Engine): Engine to connect to the database
    """
    # Execute query
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) as count_orders FROM order_level;"))
        print("Count of the rows of order_level now: " +
              str(result.fetchall()))
        result = connection.execute(
            text("SELECT COUNT(*) as count_orders FROM order_line_items;"))
        print("Count of the rows of order_level now: " +
              str(result.fetchall()))


if __name__ == "__main__":

    # xlsx_file = input("Name of the excel file: ")
    # Check if the file exists
    assert path.isfile(XLSX_FILE) is True
    # Convert the excel file to a csv file
    xlsx_data_frame: pd.DataFrame = xlsx_dataframe(XLSX_FILE)
    # Clean up the dataframe and return the required columns
    ordr_level, ordr_line_items = dataframe_cleanup(xlsx_data_frame)
    # Connect to the database
    sql_eng = create_sql_engine()
    # Insert the data into the database
    insert_databases(order_level, order_line_items, sql_eng)
    # Query the table to see the resulting number of rows
    query_table(sql_eng)
