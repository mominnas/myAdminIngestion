import pandas as pd
from typing import Dict, List, Union, Tuple, Any
from os import path



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
        quit()
    
    data_frame = pd.DataFrame(pd.read_excel(filename))
    print(data_frame.head)





if __name__ == "__main__":
    
    xlsx_file = input("Name of the excel file:  ")
    xlsx_to_csv(xlsx_file)
    