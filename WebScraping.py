from unittest import result
from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/asus-geforce-rtx-3080-rog-strix-rtx3080-o12g-gaming/p/N82E16814126550?Description=rtx%203080&cm_re=rtx_3080-_-14-126-550-_-Product"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")


prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
