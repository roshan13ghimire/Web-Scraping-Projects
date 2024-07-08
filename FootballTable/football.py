from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.common.by import By



url = "https://www.espn.com/soccer/standings/_/league/"

driver = webdriver.Chrome()

driver.get(url)

position = []
teamName = []
gamesPlayed = []
wins = []
draws = []
looses = []
goalsFor = []
goalsAgainst = []
goalDifference = []
points = []


leaugeNames = []
urlName = []


soup = BeautifulSoup(driver.page_source, 'html.parser')

for i in soup.find("select",{'aria-label':'Standings Season Type'}).findAll('option'):
    leaugeNames.append(i.getText())
    
for _ in soup.find("select",{'aria-label':'Standings Season Type'}).findAll('option'):
    urlName.append(_['value'])

myDict = {}
for j in range(len(urlName)):
    myDict[leaugeNames[j]] = urlName[j]

    
print("Choose anyone from the following options:\n")

for i in range(len(leaugeNames)):
    print(leaugeNames[i])

userInput = input()

value = myDict[userInput]


mainUrl = "https://www.espn.com/soccer/standings/_/league/" + value
driver.get(mainUrl)

soup = BeautifulSoup(driver.page_source, 'html.parser')

heading = soup.find("h1",{'class':'headline headline__h1 dib'}).getText()

# tableHead = soup.find('thead',{"class":"Table__header-group Table__THEAD"}).find('span').getText()
# position.append(soup.find("tbody",{"class":"Table__TBODY"}).findAll("tr")[0].findAll('span')[0])

# img = soup.findAll("img",{'class':'Image Logo Logo__sm'})[3]
# img

i = 0
while True:
    try:
        teamName.append(soup.find("tbody",{"class":"Table__TBODY"}).findAll("tr")[i].findAll('span')[3].getText())
        gamesPlayed.append(soup.find("div",{"class":"Table__Scroller"}).find("tr",{"data-idx":"{}".format(i)}).findAll("td")[0].find("span").getText())
        wins.append(soup.find("div",{"class":"Table__Scroller"}).find("tr",{"data-idx":"{}".format(i)}).findAll("td")[1].find("span").getText())
        draws.append(soup.find("div",{"class":"Table__Scroller"}).find("tr",{"data-idx":"{}".format(i)}).findAll("td")[2].find("span").getText())
        looses.append(soup.find("div",{"class":"Table__Scroller"}).find("tr",{"data-idx":"{}".format(i)}).findAll("td")[3].find("span").getText())
        goalsFor.append(soup.find("div",{"class":"Table__Scroller"}).find("tr",{"data-idx":"{}".format(i)}).findAll("td")[4].find("span").getText())
        goalsAgainst.append(soup.find("div",{"class":"Table__Scroller"}).find("tr",{"data-idx":"{}".format(i)}).findAll("td")[5].find("span").getText())
        goalDifference.append(soup.find("div",{"class":"Table__Scroller"}).find("tr",{"data-idx":"{}".format(i)}).findAll("td")[6].find("span").getText())
        points.append(soup.find("div",{"class":"Table__Scroller"}).find("tr",{"data-idx":"{}".format(i)}).findAll("td")[7].find("span").getText())
    except:
        break
    i += 1
df  = pd.DataFrame({'2024-2025': teamName,
                    'GP':gamesPlayed,
                    'W':wins,
                    'D':draws,
                    'L':looses,
                    'GF':goalsFor,
                    'GA':goalsAgainst,
                    'GD':goalDifference,
                    'P':points
                  }) 

df.index = range(1, len(df) + 1)
df
