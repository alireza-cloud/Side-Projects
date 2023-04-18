import requests
import re

url = 'https://philoro.at/shop/goldmuenzen/gold-philharmoniker-1-oz-2023'

# Webseite herunterladen
response = requests.get(url)
html = response.text

# Regulären Ausdruck anwenden
pattern = re.compile(r'(?<=798426">€)(.*?)(?=<)')
result = re.findall(pattern, html)

# Ergebnis auf der Konsole ausgeben
print(result)
