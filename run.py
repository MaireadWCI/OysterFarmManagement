import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta #this will calculate a date range 

#Google Sheets set up
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
try:  #exception handling-try block
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SPREADSHEET = GSPREAD_CLIENT.open('Oyster Farm Management App')

    #Open Spreadsheets
    data_entry_sheet = SPREADSHEET.worksheet("Data Entry")
    calculated_yield_sheet = SPREADSHEET.worksheet("Calculated Yield")
    orders_sheet = SPREADSHEET.worksheet("Orders")

except FileNotFoundError:   #exception handling - except block
    print("Error: The credentials file 'creds.json' was not found.")
except gspread.exceptions.SpreadsheetNotFound:
    print("Error: The spreadsheet 'Oyster Farm Management App' was not found. ")
except Exception as e:
    print(f"An unexpected error occurred: {e}")    

#welcome page on initial start up 
def welcome ():
    print("Welcome to your Oyster Farm Management system")
    main_menu()

def main_menu():  #While statements for menu choices
    while True:
        print("\nMenu Options:")
        print("1. Data Entry")
        print("2. Orders")
        print("3. Exit")
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            data_entry()
        elif choice == '2':
            orders()
        elif choice == '3':
            print ("You are no exiting the App. ")




#data = entry.get_all_values() #from love sandwiches 

#print(data) # from love sandwiches 