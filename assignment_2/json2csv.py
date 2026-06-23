import json
import csv

with open("electronics.json") as f:
    data = json.load(f)

with open("electronics.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

with open("quotes.json") as f:
    data = json.load(f)

with open("quotes.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
