import requests
from bs4 import BeautifulSoup

p = 1
for i in range(1,6):

    collectors = []
    price=[]

    result = requests.get(f"https://www.raneen.com/ar/home/home-kitchen/carpets?p={p}")
    src = result.content
    soup = BeautifulSoup(src, "html.parser")
    collector = soup.find_all("strong", {"class": "product name product-item-name"})
    prices = soup.find_all("span", {"data-price-type": "finalPrice"})

    for i in range(len(collector)):
        collectors.append(collector[i].text.strip())
        price.append(prices[i].text.strip())
    if p > 16:
        break
    print(f"page {p} is switched")
    p += 1
    print(collectors,price)
