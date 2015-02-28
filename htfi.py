import requests
import json
import csv

'''
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

'''


def add_nutrient_to_dataset(hashed, value):
	try: 
		return hashed[value][1], hashed[value][0]
	except KeyError:
		return (0, "N/A")


def get_nutrient_info(number):
	url = 'http://api.nal.usda.gov/usda/ndb/reports/?ndbno=' + number + '&type=b&format=json&api_key=mIbceHWeSHhHlYRlNX1Yc946LvZnGHjKrVRa4Mgk'
	response = requests.get(url)
	nutrients = response.json()["report"]["food"]["nutrients"]
	hashed = {}
	print nutrients
	for nutrient in nutrients:
		hashed[nutrient["name"]] = (nutrient["unit"].encode('ascii', 'ignore').decode('ascii'), nutrient["value"])

	data = [
		add_nutrient_to_dataset(hashed,"Water")[1],
		add_nutrient_to_dataset(hashed, "Water")[0],
		
		add_nutrient_to_dataset(hashed,"Energy")[1],
		add_nutrient_to_dataset(hashed,"Energy")[0],

		add_nutrient_to_dataset(hashed,"Protein")[1],
		add_nutrient_to_dataset(hashed,"Protein")[0],

		add_nutrient_to_dataset(hashed,"Total lipid (fat)")[1],
		add_nutrient_to_dataset(hashed,"Total lipid (fat)")[0],

		add_nutrient_to_dataset(hashed,"Carbohydrate, by difference")[1],
		add_nutrient_to_dataset(hashed,"Carbohydrate, by difference")[0],

		add_nutrient_to_dataset(hashed,"Fiber, total dietary")[1],
		add_nutrient_to_dataset(hashed,"Fiber, total dietary")[0],

		add_nutrient_to_dataset(hashed,"Sugars, total")[1],
		add_nutrient_to_dataset(hashed,"Sugars, total")[0],

		add_nutrient_to_dataset(hashed,"Calcium, Ca")[1],
		add_nutrient_to_dataset(hashed,"Calcium, Ca")[0],

		add_nutrient_to_dataset(hashed,"Iron, Fe")[1],
		add_nutrient_to_dataset(hashed,"Iron, Fe")[0],

		add_nutrient_to_dataset(hashed,"Magnesium, Mg")[1],
		add_nutrient_to_dataset(hashed,"Magnesium, Mg")[0],

		add_nutrient_to_dataset(hashed,"Phosphorus, P")[1],
		add_nutrient_to_dataset(hashed,"Phosphorus, P")[0],

		add_nutrient_to_dataset(hashed,"Potassium, K")[1],
		add_nutrient_to_dataset(hashed,"Potassium, K")[0],

		add_nutrient_to_dataset(hashed,"Sodium, Na")[1],
		add_nutrient_to_dataset(hashed,"Sodium, Na")[0],

		add_nutrient_to_dataset(hashed,"Zinc, Zn")[1],
		add_nutrient_to_dataset(hashed,"Zinc, Zn")[0],

		add_nutrient_to_dataset(hashed,"Vitamin C, total ascorbic acid")[1],
		add_nutrient_to_dataset(hashed,"Vitamin C, total ascorbic acid")[0],

		add_nutrient_to_dataset(hashed,"Thiamin")[1],
		add_nutrient_to_dataset(hashed,"Thiamin")[0],
		
		add_nutrient_to_dataset(hashed,"Riboflavin")[1],
		add_nutrient_to_dataset(hashed,"Riboflavin")[0],
		
		add_nutrient_to_dataset(hashed,"Niacin")[1],
		add_nutrient_to_dataset(hashed,"Niacin")[0],

		add_nutrient_to_dataset(hashed,"Vitamin B-6")[1],
		add_nutrient_to_dataset(hashed,"Vitamin B-6")[0],

		add_nutrient_to_dataset(hashed,"Folate, DFE")[1],
		add_nutrient_to_dataset(hashed,"Folate, DFE")[0],

		add_nutrient_to_dataset(hashed,"Vitamin B-12")[1],
		add_nutrient_to_dataset(hashed,"Vitamin B-12")[0],

		add_nutrient_to_dataset(hashed,"Vitamin A, RAE")[1],
		add_nutrient_to_dataset(hashed,"Vitamin A, RAE")[0],

		add_nutrient_to_dataset(hashed,"Vitamin A, IU")[1],
		add_nutrient_to_dataset(hashed,"Vitamin A, IU")[0],


		add_nutrient_to_dataset(hashed,"Vitamin E (alpha-tocopherol)")[1],
		add_nutrient_to_dataset(hashed,"Vitamin E (alpha-tocopherol)")[0],

		add_nutrient_to_dataset(hashed,"Vitamin D (D2 + D3)")[1],
		add_nutrient_to_dataset(hashed,"Vitamin D (D2 + D3)")[0],

		add_nutrient_to_dataset(hashed,"Vitamin D")[1],
		add_nutrient_to_dataset(hashed,"Vitamin D")[0],

		add_nutrient_to_dataset(hashed,"Vitamin K (phylloquinone)")[1],
		add_nutrient_to_dataset(hashed,"Vitamin K (phylloquinone)")[0],

		add_nutrient_to_dataset(hashed,"Fatty acids, total saturated")[1],
		add_nutrient_to_dataset(hashed,"Fatty acids, total saturated")[0],

		add_nutrient_to_dataset(hashed,"Fatty acids, total monounsaturated")[1],
		add_nutrient_to_dataset(hashed,"Fatty acids, total monounsaturated")[0],
		add_nutrient_to_dataset(hashed,"Fatty acids, total polyunsaturated")[1],
		add_nutrient_to_dataset(hashed,"Fatty acids, total polyunsaturated")[0],
		add_nutrient_to_dataset(hashed,"Cholesterol")[1],
		add_nutrient_to_dataset(hashed, "Cholesterol")[0]
	]
	return data

def get_data():
	all_data = []
	with open('ingredients.csv', 'rU') as csvfile:
	    reader = csv.reader(csvfile, dialect=csv.excel_tab)
	    for row in reader:
	    	if '#' not in row[0]:
		    	q_parameter = row[0].replace(' ', '+').replace(",", '')
		    	url = 'http://api.nal.usda.gov/usda/ndb/search/?format=json&api_key=mIbceHWeSHhHlYRlNX1Yc946LvZnGHjKrVRa4Mgk&nutrients=205&q=' + q_parameter
		    	response = requests.get(url)
		    	print "Next Item, Searching For: " + row[0]
		    	if response.json().get("errors"):
			    	print "nothing found for ingredient: ", q_parameter
		    	else:
			    	for i, item in enumerate(response.json()['list']['item']):
						print i,".", item['name'], ", Code Number: ", item['ndbno']
		    		s = raw_input('Indicate which ingredient to choose by picking a number. Press Enter once you type in the number. \n')
		    		while(int(s) >= len(response.json()['list']['item'])):
		    			s = raw_input(' The number you indicated is out of range. Please try again.\n')
		    		print "You selected: ", response.json()['list']['item'][int(s)]['name'], '\n'
		    		print "Adding it to your CSV\n"
		    		row = [response.json()['list']['item'][int(s)]['name'], 
		    		response.json()['list']['item'][int(s)]['ndbno']] + get_nutrient_info(response.json()['list']['item'][int(s)]['ndbno'])
		    		all_data.append(row)
		    		print "\n" 
	return all_data

if __name__ == '__main__':
	with open('processed.csv', 'a') as csvfile:
	    fieldnames = [
	    'Name', 
	    'Code', 
		'Water Units',
		'Water',
		'Energy Units',
		'Energy',
		'Protein Units',
		'Protein',
		'Total lipid (fat) Units',
		'Total lipid (fat)',
		'Carbohydrate, by difference Units',
		'Carbohydrate, by difference',
		'Fiber, total dietary Units',
		'Fiber, total dietary',
		'Sugars, total Units',
		'Sugars, total',
		'Calcium, Ca Units',
		'Calcium, Ca',
		'Iron, Fe Units',
		'Iron, Fe',
		'Magnesium, Mg Units',
		'Magnesium, Mg',
		'Phosphorus, P Units',
		'Phosphorus, P',
		'Potassium, K Units',
		'Potassium, K',
		'Sodium, Na Units',
		'Sodium, Na',
		'Zinc, Zn Units',
		'Zinc, Zn',
		'Vitamin C, total ascorbic acid Units',
		'Vitamin C, total ascorbic acid',
		'Thiamin Units',
		'Thiamin',
		'Riboflavin Units',
		'Riboflavin',
		'Niacin Units',
		'Niacin',
		'Vitamin B-6 Units',
		'Vitamin B-6',
		'Folate, DFE Units',
		'Folate, DFE',
		'Vitamin B-12 Units',
		'Vitamin B-12',
		'Vitamin A, RAE Units',
		'Vitamin A, RAE',
		'Vitamin A, IU Units',
		'Vitamin A, IU',
		'Vitamin E (alpha-tocopherol) Units',
		'Vitamin E (alpha-tocopherol)',
		'Vitamin D (D2 + D3) Units',
		'Vitamin D (D2 + D3)',
		'Vitamin D Units',
		'Vitamin D',
		'Vitamin K (phylloquinone) Units',
		'Vitamin K (phylloquinone)',
		'Fatty acids, total saturated Units',
		'Fatty acids, total saturated',
		'Fatty acids, total monounsaturated Units',
		'Fatty acids, total monounsaturated',
		'Fatty acids, total polyunsaturated Units',
		'Fatty acids, total polyunsaturated',
		'Cholesterol Units'
		'Cholesterol'
		]
	    writer = csv.writer(csvfile)
	    writer.writerow(fieldnames)
	    writer.writerows(get_data())
