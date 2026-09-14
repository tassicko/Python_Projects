import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
response = requests.get('https://www.arogga.com/category-home/medicines', headers= headers).text

soup = BeautifulSoup(response, 'lxml')
meds= soup.find_all('li', class_='max-w-33.25 min-w-33.25 md:max-w-54.75 md:min-w-54.75')

name= []
price= []
discount_price= []

for i in meds:
    meds_name = i.find('h4', class_='text-xs md:text-base mb-2 font-semibold line-clamp-2')
    name.append(meds_name.text.strip())

    meds_real_price= i.find('del', class_='text-[10px] md:text-sm text-gray-600 font-medium product_single_mrp_generate')
    price.append(meds_real_price.text.strip())

    meds_real_price = i.find('div',class_='font-semibold text-xs md:text-base product_single_price_generate')
    discount_price.append(meds_real_price.text.strip())

# print(name)
# print(price)
# print(discount_price)

d={'Name':name,'Price':price,'Discount Price':discount_price}#
df= pd.DataFrame(d)
print(df)
df.to_csv('Homepage_Medicine.csv')