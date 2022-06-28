from bs4 import BeautifulSoup
import requests

URL = "https://coinmarketcap.com/"

result = requests.get(URL).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

# print(trs[1].previous_sibling)  # önceki content'i verir
# print("\n--------------------------------------\n")
# print(trs[0].next_sibling)  # sonraki content'i verir

prices = {}


for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixedName = name.p.string
    fixedPrice = price.a.string
    prices[fixedName] = fixedPrice
print(prices)
