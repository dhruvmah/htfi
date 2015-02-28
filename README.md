# htfi
Healthy Food Truck Initiative Script

Built by Hack4Impact for the Healthy Food Truck Initiative

This script reads in a file consisting of types of ingredients (each ingredient on its own line) and then generates a
CSV file that writes out the nutrients associated with each ingredient. This relies on the USDA Nutrient API and since there
are many types of similar ingredients (ie. Bagel, eggs and Bagel, onions), the user of this script must indicated which ingredient
search result they want entered into their database. 

In order to add new ingredients to an existing spreadsheet, simply create a new file called "ingredients.csv", with each new
ingredient on a new line. As the code runs, it will add new rows to any file called "processed.csv", as long as it is located
in the same folder directory as the code. If the file does not exist, it will create a new one, called "processed.csv".

You can run this file by opening Terminal, navigating to the folder in which this file is located, and typing "python htfi.py"

For any questions, please contact us at admin@hack4impact.org
