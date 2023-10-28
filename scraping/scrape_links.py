import requests
from bs4 import BeautifulSoup
import json

links_list = []
for i in range(40):
    try:
        url = f"https://indiankanoon.org/search/?formInput=doctypes%3A%20judgments%20fromdate%3A%201-1-2023%20todate%3A%2031-12-2023&pagenum={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all("a")
        links = [str(results[i]) for i in range(len(results)) if "/docfragment" in str(results[i])]
        links_list.append(links)
    except Exception as e:
        pass

with open('links.json', 'w') as f:
    json.dump(links_list, f)