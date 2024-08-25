### download template for website from google sheets and save in folder.  run script to update cocktails on website




import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Create an empty list to store the data (no keys)
    data_list = []

    # Step 1: Open the CSV file using a file handler
    with open(csv_file_path, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        # Convert each row into a dictionary and add it to the data_list
        for row in csv_reader:
            data_list.append(row)

    # Step 2: Open the JSON file using a JSON file handler
    with open(json_file_path, 'w', encoding='utf-8') as json_file_handler:
        # Step 3: Write the data_list to the JSON file
        json.dump(data_list, json_file_handler, indent=4)

# Specify the paths for your CSV and JSON files
csv_file_path = r'template for website - Sheet1.csv'
json_file_path = r'cocktail-recipes.json'
#for test purposes
#json_file_path = r'cocktail-recipes_test1.json'

# Call the function to convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)

# Call the function to convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)

print(f"Conversion completed! Data saved to {json_file_path}")



# Read the existing JSON data from the file
input_file_path = "cocktail-recipes.json"
output_file_path = "cocktail-recipes.json"

with open(input_file_path, "r") as json_file:
    data = json.load(json_file)

# Convert ingredients from comma-separated string to a list
for entry in data:
    ingredients_str = entry["ingredients"]
    ingredients_list = ingredients_str.split(",")
    entry["ingredients"] = ingredients_list


# Save the modified data back to a new JSON file
with open(output_file_path, "w") as json_output_file:
    json.dump(data, json_output_file, indent=4)

print(f"Modified data saved to {output_file_path}")
