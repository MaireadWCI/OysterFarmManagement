
## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


project 3 template added 
gspread 
auth
sheets
added worksheet 
gitnore
requirements

#Oyster Farm Management process App



This is a Python App for an Oyster Farm. It is designed to accompany a website for an Oyster farm business. The App is intended for the Business owner  be to able to track rows of trestles, monitor the amount, type, when and where the bags of oysters are places so based on different variables will be ready in a certain time. 

#User Experience Design

## User Stories
As a user of this App:
* I would like to add data to a spreadsheet to record what has been laid. 
* I would like to ensure I have entered the all nessesary data by confirmation. 
* I would like to be able to retrieve data from my spreadsheet.
* I would like to be able to enter the date orders are due
* I would like to get return data on what rows to harvest along with their corresponding dates
* I would like to get the return dates to be all within the same month as date I enter. 

## Colour Scheme
<p>A combination of colours were chosen to represent the feel of the ocean and remain on theme with the brands identity.</p>

![Color scheme](./assets/images/readme/color-theme.png)

![Lucidchart Diagram](/idsflowchart_2.png)

# Features
### Welcome Message: 
 Display a welcome message upon opening.
### Menu Options:
 Three main options - Data Entry and Orders or Exit application. 
### Data Entry: 
Input details about oyster bags.
### Data validation:
Functions to validate the format of dates and other inputs before logging them to spreadsheet. 
### Orders: 
Retrieve information about ready oysters based on user input.
### Google Sheets Integration: 
Connects to Google Sheets using gspread and oauth2client.
### Console Interaction: 
The application interacts with the user through standard input and output in the terminal.