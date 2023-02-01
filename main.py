import pandas as pd
from typing import Dict, List, Union, Tuple, Any
from os import path



def xlsx_to_csv(filename: str):
    """ Given a filename, converts the excel file to a proper comma seperated file.

    Args:
        filename (str): name of the excel file 
    """
    
    # Basic error handling
    if ".xlsx" not in file_name:
        print("Assuming xlsx extension")
        file_name = file_name + ".xlsx"
    if not path.isfile(file_name):
        print("Invalid file")
        
    data_frame = pd.DataFrame(pd.read_excel(filename))
    print(data_frame.head)





if __name__ == "__main__":
    