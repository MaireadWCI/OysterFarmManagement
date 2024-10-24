from colorama import init, Fore, Style
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta  # this will calculate a date range
import re  # supports regular expressions ie search, manipulate and validate.

# initialise colorama
init(autoreset=True)

# Google Sheets set up
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

try:  # exception handling-try block
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SPREADSHEET = GSPREAD_CLIENT.open('Oyster Farm Management App')

    # Open Spreadsheets
    data_entry_sheet = SPREADSHEET.worksheet("Data Entry")
    calculated_yield_sheet = SPREADSHEET.worksheet("Calculated Yield")
    orders_sheet = SPREADSHEET.worksheet("Orders")

except FileNotFoundError:   # exception handling - except block
    print("Error: The credentials file 'creds.json' was not found.")
except gspread.exceptions.SpreadsheetNotFound:
    print("Error: Spreadsheet 'Oyster Farm Management App' was not found.")
except Exception as e:
    print(Fore.RED + f"An unexpected error occurred: {e}")


def validate_data(date, row, oyster_type, amount):
    """method to validate date, row , oyster type, and amount"""
    print(
        f"Validating: date={date}, row={row}," +
        "oyster_type={oyster_type}, amount={amount}")

    # validate date
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print(Fore.RED + "Invalid date format. Please use YYYY-MM-DD")
        return False

    # Validate row
    row = row.upper()  # converts the row letters to uppercase.

    if not re.match(r'^[A-Z]\d{2}$', row):
        print(Fore.RED + "Invalid row format. Please use a format like C02")
        return False

    # Validate oyster type
    oyster_type = oyster_type.lower()  # converts data to lower case.
    if oyster_type not in ['seed', 'half-grown']:
        print(
            Fore.RED + "Invalid oyster type." +
            "Please enter 'seed' or 'half-grown'.")
        return False

    # Validate amount to positive intreger
    if not amount.isdigit() or int(amount) <= 0:
        print(Fore.RED + "Invalid amount. Please enter a positive number.")
        return False

    return True


# welcome page on initial start up
def welcome():
    print(Fore.GREEN + "Welcome to your Oyster Farm Management system")
    main_menu()


def main_menu():  # While statements for menu choices
    while True:
        print(Fore.GREEN + "\nMenu Options:\n")
        print("1. Data Entry (To log laying of oysters on Tressles)")
        print("2. Orders (To assess what rows are available for harvesting)")
        print("3. Exit (Do you wish to leave the App)\n")

        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            data_entry()
        elif choice == '2':
            orders()
        elif choice == '3':
            print(Fore.GREEN + "You are now exiting the App. ")
            break
        else:
            print(Fore.RED + "Invalid option. Please select a Valid option")


def data_entry():   # data entry input field with format examples
    """Loops until correct data entered"""

    while True:
        # prompt for date entry
        date = input("Enter date: (YYYY-MM-DD)\n").strip()
        try:
            # validate date format immediately
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print(Fore.RED + "Invalid date format. Please use YYYY-MM-DD")
            continue  # restart the loop for date entry

        # loop until valid row is entered
        while True:
            row = input(
                "Enter row: (ie C04- one letter and two digits)\n").strip()
            row = row.upper()  # converts to upper for validation
            if re.match(r'^[A-Z]\d{2}$', row):
                break  # Exit loop if valid
            print(
                Fore.RED + "Invalid row format" +
                "please use one letter and two digits ie C02")

        # loop until valid oyster type entered
        while True:
            oyster_type = input(
                "Enter type (seed or half-grown)\n").strip().lower()
            if oyster_type in ['seed', 'half-grown']:
                break  # exit the loop if valid
            print(
                Fore.RED + "Invalid type. Please enter 'seed' or 'half-grown'")

        # Loop until a valid amount is entered
        while True:
            amount = input("Enter number of bags\n").strip()
            if amount.isdigit() and int(amount) > 0:
                break  # exit loop if valid
            print(Fore.RED + "Invalid amount. Please enter a positive number.")

    # If all data is validated append to google sheets.
        data_entry_sheet.append_row([date, row, oyster_type, amount])
        print(Fore.GREEN + "Data has been logged successfully.")
        break  # loops ends after successful entry  - remove if not needed


def orders():  # define orders section
    """Method to select order date, validate and to retieve
     15 days on either side of date also"""

    while True:  # exception handling
        required_date = input("Enter the required date (YYYY-MM-DD):").strip()

        # if validate_date(required_date): #data validation
        try:
            required_date_dt = datetime.strptime(required_date, '%Y-%m-%d')
            start_date = required_date_dt - timedelta(days=15)
            end_date = required_date_dt + timedelta(days=15)

            ready_oysters = calculated_yield_sheet.get_all_records()
            print(
                Fore.GREEN + "\nReady Oysters" +
                " within 15 days of the date entered")

            found_ready_oysters = False  # to track if oysters are found
           
            for record in ready_oysters:
                date_ready_value = record['Date Ready']

                # if not isinstance(date_ready_value, str):
                # continue

                record_date = datetime.strptime(
                    record['Date Ready'], '%Y-%m-%d')

                if start_date <= record_date <= end_date:
                    print(
                        f"Row: {record['Row']}" +
                        f"  Date Ready: {record['Date Ready']}")

                    found_ready_oysters = True  # flag to true if record found

            if not found_ready_oysters:
                print(
                    Fore.RED +
                    "No oysters ready within the specified date range")

            break  # ends loop after order is processed.
        except ValueError:
            print(Fore.RED + "Incorrect date format entered. Please try again")


welcome() # start application




