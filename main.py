import sys
import pandas as pd
from typing import Dict, List, Union, Tuple, Any
from os import path
import mysql.connector as msql
from mysql.connector import Error
import cred

xlsx_file = cred.xlsx_file


def xlsx_to_csv(filename: str) -> None:
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
    data_frame = pd.DataFrame(data)
    print(data_frame.head)



def sql_connect():

    try:
        conn = msql.connect(host=cred.DEFAULT_HOST, user=cred.DEFAULT_USER, 
                            password=cred.DEFAULT_PWD)#give ur username, password
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE employee")
            print("Database is created")
    except Error as e:
        print("Error while connecting to MySQL", e)




if __name__ == "__main__":
    
    #xlsx_file = input("Name of the excel file: ")
    
    assert path.isfile(xlsx_file) is True
    xlsx_to_csv(xlsx_file)
    sql_connect()
    