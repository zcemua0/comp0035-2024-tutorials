mock_database = {
    1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
    42: {'name': 'Bob', 'email': 'bob@example.com', 'age': 45},
}

import sys
from pathlib import Path
import pandas as pd

def describe_dataframe(df):
    print(df.describe())
    print(df.shape)

if __name__ == '__main__':
    
    # Locate the data file `paralmpics_raw.csv` and npc files relative to
    # this file using pathlib.Path. 
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath(
        "data", "paralympics_events_raw.csv"
    )
    paralympics_datafile_excel = Path(__file__).parent.parent.joinpath(
        "data", "paralympics_all_raw.xlsx"
    )
    npc_csv = Path(__file__).parent.parent.joinpath("data", "npc_codes.csv")
    
    # Error handling for the file read
    try:
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")
    
    # Read the data from the files into a Pandas dataframe. 
    events_csv_df = pd.read_csv(paralympics_datafile_csv)
    events_excel_df = pd.read_excel(paralympics_datafile_excel)
    medal_standings_df = pd.read_excel(paralympics_datafile_excel, sheet_name="medal_standings")
    
    # Call the function to describe the dataframe
    describe_dataframe(events_csv_df)
     
        
    # The functions are in the modules in mypkg2. You will need to import them.
    from tutorialpkg.mypkg2.mymodule2_1 import calculate_area_of_circle
    from tutorialpkg.mypkg2.mymodule2_2 import fetch_user_data
    
    # Calculate the area of a circle with a radius of 10. Print the result.
    area = calculate_area_of_circle(10)
    print(f"The area is {area}.")

    # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
    print(fetch_user_data(42, mock_database))
