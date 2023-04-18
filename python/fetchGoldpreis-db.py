import requests
import re
import pymongo

# Verbindung zur MongoDB-Datenbank herstellen
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["goldmuenzen"]

# Webseite herunterladen
url = 'https://philoro.at/shop/goldmuenzen/gold-philharmoniker-1-oz-2023'
response = requests.get(url)
html = response.text

# Regulären Ausdruck anwenden
pattern = re.compile(r'(?<=798426">€)(.*?)(?=<)')
result = re.findall(pattern, html)

# Ergebnis in die Sammlung einfügen
doc = {"price": result[0]}
collection.insert_one(doc)

# Verbindung zur MongoDB-Datenbank schließen
client.close()
