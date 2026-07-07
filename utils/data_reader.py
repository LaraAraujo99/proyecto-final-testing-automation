import csv
import json

# Lee archivo csv/json para poder usar los datos
def read_users_csv():
    with open("data/users.csv", newline="") as file:
        # Convertir en diccionario
        reader = csv.DictReader(file)
        # Return del diccionario en forma de lista
        return list(reader)
    
def read_products_json():
    with open("data/products.json") as file:
        return json.load(file)
    
    