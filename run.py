import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta #this will calculate a date range 
import re #provides support for working with regular expressions ie search, manipulate and validate. 

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

#validation of data function
def validate_data(date, row, oyster_type, amount):
    #validate date
    try:
        datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")
            return False

    #Validate row


    #Validate oyster type
    if oyster_type not in ['seed', 'half-grown']:
        print("Invalid oyster type. Please enter 'seed' or 'half-grown'.")
        return False

    #Validate amount to positive intreger
    if not amount.isdigit() or int(amount) <= 0:
        print("Invalid amount. Please enter a positive number.")
        return False


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
            print ("You are now exiting the App. ")
            break

def data_entry():   #data entry input field with format examples
    while True:
        date = input("Enter date: (YYYY-MM-DD)\n")
        row = input("Enter row: (ie C04)\n")
        oyster_type = input("Enter type (seed or half-grown)\n")
        amount = input("Enter number of bags\n")

        if validate_data(date, row, oyster_type, amount):
            data_entry_sheet.append_row([date, row, oyster_type, amount])
            print("Data has been logged successfully.")
            break #loops ends after successful entry
        else:
            print("Incorrect data format entered. Please try again using this format yyyy-mm-dd")
            

def orders():  #define orders section

    while True:  #exception handling
        required_date - input("Enter the requited date (YYY-MM-DD):")

        if validate_date(required_date): #data validation 
            required_date_dt = datetime.strptime(required_date, '%Y-%M-%D' )
            start_date = required_date_dt - timedelta(days=15) #to retieve 15 days on either side of date also 
            end_date = required_date_dt +timedelta(days=15)

            ready_oysters = calculated_yield_sheet.get_all_records()
            print("\nReady Oysters within 15 days of the date entered")
            for record in ready_oysters:
                record_date = datetime.strptime(record['Date Ready'], '%Y-%m-%d')
                if start_date <= record_date <= end_date:
                    print(f"Row: {record['Row']} Date Ready:{record['Date Ready']}")
            break
        else: 
            print("incorrect date format entered. Please try again")

welcome()
