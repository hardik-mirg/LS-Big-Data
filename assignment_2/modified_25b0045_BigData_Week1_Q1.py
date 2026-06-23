import json
import requests

url = "https://fakestoreapi.com/products"

response = requests.get(url)
if response.status_code == 200:
    # raw dataset
    data = response.json() 
    # only required fields
    filtered = [{"id": product['id'], "title": product['title'], "price": product['price'], "category": product['category']} for product in data]
    # electronics items with price > 50
    premium = [product for product in filtered if product['category'] == 'electronics' and product['price'] > 50]

    with open("./electronics.json", "w") as f:
        json.dump([product for product in premium], f, indent=4)
else:
    print(f"Invalid Reponse. Status code: {response.status_code}")