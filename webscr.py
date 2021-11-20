from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

browser = webdriver.Chrome(
    "C:/Users/jjtam/Downloads/chromedriver_win32/chromedriver.exe")
startUrl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser.get(startUrl)
time.sleep(10)


def scrapData():
    headers = ["Name", "Light_years_from_Earth",
               "planet_mass", "Stellar_Magnitude", "Discovery_Date"]
    planets = []
    for i in range(0, 50):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        allUl = soup.find_all("ul", attrs={"class", "exoplanet"})
        for eachul in allUl:
            allLi = eachul.find_all("li")
            templist = []
            for index, eachli in enumerate(allLi):
                if index == 0:
                    templist.append(eachli.find_all("a")[0].contents[0])
                else:
                    templist.append(eachli.contents[0])
            planets.append(templist)
            browser.find_element_by_xpath(
                '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("Scraper.csv","w",newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planets)
scrapData()
