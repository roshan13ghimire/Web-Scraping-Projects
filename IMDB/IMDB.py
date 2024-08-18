import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

title = []
year = []
rating = []
voteCount = []
length =[]

yearInput = input("Give any year to search the movies in that year: ")
print("\nTop 25 movies in " + yearInput + " are:")

url = "https://www.imdb.com/search/title/?release_date=" + yearInput



HEADERS = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
response = requests.get(url,headers=HEADERS)

soup = BeautifulSoup(response.text, 'html.parser')
for i in soup.findAll("li", {"class": "ipc-metadata-list-summary-item"}):
    try:
        title.append(i.find("div",{"class","ipc-title"}).getText())
    except:
        title.append("NULL")
    try:
        year.append(i.find("span",{"class","sc-b189961a-8"}).getText())
    except:
        year.append("NULL")
    try:
        rating.append(i.find("span",{"class","ipc-rating-star--rating"}).getText())
    except:
        rating.append("NULL")
    try:
        voteCount.append(i.find("span",{"class","ipc-rating-star--voteCount"}).getText())
    except:
        voteCount.append("NULL")
    a = i.find("div", {"class": "sc-b189961a-7 btCcOY dli-title-metadata"})
    if(len(a) >= 2):
        try:
            b = a.findAll('span')[1].getText()
            if('h' in b or 'm' in b):
                length.append(b)
            else:
                length.append("NULL")
        except:
            length.append("NULL")
    else:
        length.append("NULL")

        
df = pd.DataFrame({'Title':title,
                 'Year':year,
                 'Rating':rating,
                 'Vote Count':voteCount,
                 'Length':length})
df['Title'] = df['Title'].apply(lambda x: re.sub(r'^\d+\.\s*', '', x))
df