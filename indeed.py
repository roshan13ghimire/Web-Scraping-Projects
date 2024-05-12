from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.common.by import By

jobName = input()
placeName = input()

jobTitle = []
companyName = []
jobLocation = []

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

page = 10000

url = "https://ca.indeed.com/jobs?q=" + jobName + "&l=" + placeName + "&start=" + str(page)

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
try:
    lastPageNumber = int(soup.find("a",{"data-testid":"pagination-page-current"}).getText())
    lastPageNumber = (lastPageNumber) * 10
except:
    lastPageNumber = 0
page = 0


while(page <= lastPageNumber):
    url = "https://ca.indeed.com/jobs?q=" + jobName + "&l=" + placeName + "&start=" + str(page)
    driver.get(url)
        
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        driver.find_element_by_class_name('css-yi9ndv').click()
        for _ in soup.findAll("h2",{"class": "jobTitle css-198pbd eu4oa1w0"}):
            jobTitle.append(_.find("span").getText())
        for _ in soup.findAll("span",{"data-testid":"company-name"}):
            companyName.append(_.getText())
        for _ in soup.findAll("div",{"data-testid":"text-location"}):
            jobLocation.append(_.getText())
        page += 10
    except:
        for _ in soup.findAll("h2",{"class": "jobTitle css-198pbd eu4oa1w0"}):
            jobTitle.append(_.find("span").getText())
        for _ in soup.findAll("span",{"data-testid":"company-name"}):
            companyName.append(_.getText())
        for _ in soup.findAll("div",{"data-testid":"text-location"}):
            jobLocation.append(_.getText())
        page += 10
        

    

df  = pd.DataFrame({'Job Title': jobTitle,
                  'Company Name': companyName,
                  'Location': jobLocation,
                  }) 

df
