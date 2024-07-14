from selenium import webdriver
from bs4 import BeautifulSoup
import time
from datetime import date

def get_espn_soccer_scores():
    todayDate = str(date.today())
    actualDate = todayDate.replace('-', '')
    url = "https://www.espn.com/soccer/scoreboard/_/date/" + actualDate

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(5)
    results = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')


    dateWithDay = soup.find("h3", {'class': 'Card__Header__Title Card__Header__Title--no-theme'}).getText()
    results.append(dateWithDay + "\n")

    
    
    for i in soup.findAll("section", {'class': 'Card gameModules'}):
        z = []
        y = []
        w = []
        x = []

        a = i.find("h3", {'class': 'Card__Header__Title Card__Header__Title--no-theme'})
        y.append(a.getText())

        for q in i.findAll("div", {'class': 'ScoreCell__Time ScoreboardScoreCell__Time h9 clr-negative'}):
            z.append(q.getText()) 
        for p in i.findAll("div", {'class': 'ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-03'}):
            z.append(p.getText()) 
        for o in i.findAll("div", {'class': 'ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-01'}):
            z.append(o.getText())
        for k in i.findAll("div", {'class': 'ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db'}):
            w.append(k.getText())
        for j in i.findAll("div", {'class': 'ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2'}):
            x.append(j.getText())
            
        for a in range(len(y)):
            results.append(y[a])
            if len(x) != 0:
                bb = 0
                cc = 0
                for b in range(len(z)):
                    if len(z[b]) == 2 or "'" in z[b]:
                        result_line = f"{z[b]} {w[cc]} - {w[cc + 1]} : {x[bb]} - {x[bb+1]}"
                        results.append(result_line)
                        bb += 2
                        cc += 2
                    else:
                        result_line = f"{z[b]} {w[cc]} - {w[cc + 1]}"
                        results.append(result_line)
                results.append("\n")
            else:
                cc = 0
                for b in range(len(z)):
                    result_line = f"{z[b]} {w[cc]} - {w[cc + 1]}"
                    results.append(result_line)
                    cc += 2
                results.append("\n")
    res = ""
    for result in results:
        res += result + "\n"
    return res

