import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"
response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")
all_quotes = soup.find_all("div", class_="quote")

quotes = []

for quote in all_quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    quotes.append({"text": text, "author": author})

with open('./quotes.json', 'w') as file:
    json.dump([quote for quote in quotes], file, indent=4)