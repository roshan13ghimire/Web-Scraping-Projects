from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

itemName = input("Enter the item that you want to search: ")

chrome_options = Options()
chrome_options.add_argument("--headless") 

driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.amazon.com/s?k=' + itemName + '&page=1'

driver.get(url)

title = []
rating = []
ratings = []
price = []
delivery = []


soup = BeautifulSoup(driver.page_source, 'html.parser')

lastPage = soup.find('span',{'class':'s-pagination-item s-pagination-disabled'}).getText() 
for details in tqdm(range(1,int(lastPage)),desc="Scraping details"):
    for i in soup.findAll('div',{'data-csa-c-type':'item'}):
        try:
            titleText = i.find('span',{'class':'a-size-medium a-color-base a-text-normal'}).getText()
            title.append(titleText)
        except:
            titleText = "No title"
            title.append(titleText)
        try:  
            ratingText = i.find('span',{'class':'a-icon-alt'}).getText()
            rating.append(ratingText)
        except:
            ratingText = "No Stars"
            rating.append(ratingText)
        try:
            ratingsText = i.find('span',{'class':'a-size-base s-underline-text'}).getText()
            ratings.append(ratingsText + ' ratings')
        except:
            ratingsText = "No ratings given"
            ratings.append(ratingsText)
        try:
            priceText =i.find('span',{'data-a-color':'base'}).find('span',{'class':'a-offscreen'}).getText()
            price.append(priceText)
        except:
            priceText = "No price given"
            price.append(priceText)
        try:
            deliveryText = i.find('span',{'class':'a-color-base a-text-bold'}).getText()
            delivery.append(deliveryText)
        except:
            deliveryText = "No delivery date given"
            delivery.append(deliveryText)
df = pd.DataFrame({'Title':title,
                 'Stars':rating,
                 'Ratings':ratings,
                 'Price':price,
                 'Delivery Date':delivery})
df
