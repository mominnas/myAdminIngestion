import sys
import pandas as pd
from typing import Dict, List, Union, Tuple, Any
from os import path
import mysql.connector as msql
from mysql.connector import Error
import sqlalchemy as db
import pymysql

import cred

xlsx_file = cred.xlsx_file

order_level: pd.DataFrame = pd.DataFrame(None)
order_line_items: pd.DataFrame = pd.DataFrame(None)


ORDER_LEVEL_COLUMNS = ['order_reference', 'first_name', 'last_name', 'company', 'address1',
                       'address2', 'city', 'province_state', 'postal_zip', 'country',
                       'phone_number', 'additional_info', 'preferred_shipping_service',
                       'status', 'ship_complete']


ORDER_LINE_ITEMS_COLUMNS = ['order_reference', 'preferred_supplier', 'product_supplier_reference', 'product_quantity',
                            'part_order_status',
                            'shipping_service',
                            'tracking_number']


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
    """ Given a filename, converts the excel file to a proper comma seperated file.

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
    df = pd.DataFrame(data)
    # print(data_frame.head)
    return df


def dataframe_cleanup(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """ Cleans up the dataframe and returns a dataframe with the required columns.

    Returns:
        pd.DataFrame: Two dataframes with the required columns, one for each table.
    """

    # Change column names to compatible sql names from the schema
    df = df.rename(columns=sql_mapping)

    
    # Drop all the unnecessary columns from the dataframe for order_level
    df1 = df[df.columns.intersection(ORDER_LEVEL_COLUMNS)]

    columns: List = df1.columns.values.tolist()
    print(columns)

    if (not all(columns)):
        print("Columns are not correct")
        sys.exit()


    # Drop all the unnecessary columns from the dataframe for order_level
    df2 = df[df.columns.intersection(ORDER_LINE_ITEMS_COLUMNS)]

    columns: List = df2.columns.values.tolist()
    print(columns)

    if (not all(columns)):
        print("Columns are not correct")
        sys.exit()


    return df1, df2





def sql_connect():

    try:
        conn = msql.connect(host=cred.DEFAULT_HOST, user=cred.DEFAULT_USER,
                            password=cred.DEFAULT_PWD, port=3306, database=cred.DATABASE_NAME)  # give ur username, password
        # db_Info = conn.get_server_info()
        # print("Connected to MySQL Server version ", db_Info)
        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM order_level")
            print("Database is created")
    except Error as e:
        print("Error while connecting to MySQL", e)



def pysql_connect() -> None:
    
    # database connection
    connection = pymysql.connect(host=cred.DEFAULT_HOST, port=8889, user=cred.DEFAULT_USER, passwd=cred.DEFAULT_PWD, database=cred.DATABASE_NAME)
    cursor = connection.cursor()
    # some other statements with the help of cursor
    connection.close()




if __name__ == "__main__":

    # xlsx_file = input("Name of the excel file: ")

    assert path.isfile(xlsx_file) is True

    data_frame: pd.DataFrame = xlsx_dataframe(xlsx_file)
    
    order_level, order_line_items = dataframe_cleanup(data_frame)
    
    #print(order_line.head())
    #sql_connect()
    pysql_connect()
