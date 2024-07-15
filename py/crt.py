import requests
from bs4 import BeautifulSoup

req = requests.get("https://crt.sh/?q=dyson.ae")

soup = BeautifulSoup(req.text,"html.parser")

tr_elements = soup.find_all("tr")
results = []

for tr in tr_elements:
    td_elements = tr.find_all("td")
    selection = []
    for element in td_elements :
        if element.string and "dyson" in element.string:
            selection.append(element.string.strip())

    if len(selection) == 2 :
        results.append(tuple(selection))

for result in results:
    print(result)
