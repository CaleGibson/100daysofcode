
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
service = Service(r"C:\Users\cale1\Python\ChromeDriver\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
form_link = "https://docs.google.com/forms/d/e/1FAIpQLSeoJVGAaTSKZTwmgo6ZsI18frBXR6k935YRvyhyF41xsZNyag/viewform?usp=sf_link"
driver.get(form_link)

response = requests.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.68773116064453%2C%22east%22%3A-122.17892683935547%2C%22south%22%3A37.55080116062149%2C%22north%22%3A37.9991021505461%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers=header)
rent_page = response.text

soup = BeautifulSoup(rent_page, "html.parser")
info = soup.find_all(class_="property-card-data")


result_list = []
for listing in info:
    url = listing.select_one(".property-card-link").get("href")
    address = listing.find(name='address').text
    price = listing.find(name="span").text
    result_list.append({
        "address": address,
        "url": url,
        "price": price,
    })

for each in result_list:
    string = each.get('url')
    if string[0] == '/':
        each['url'] = f"https://www.zillow.com{string}"



for listing in result_list:
    address_input = driver.find_element(By.XPATH, '// *[ @ id = "mG61Hd"] / div[2] / div / div[2] / div[1] / div / div / div[2] / div / div[1] / div / div[1] / input')
    url_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address_input.send_keys(listing['address'])
    url_input.send_keys(listing['url'])
    price_input.send_keys(listing['address'])
    submit.click()
    time.sleep(1)
    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(2)
#//*[@id="SMMuxb"]/a[1]
#//*[@id="identifierId"]
#//*[@id="identifierNext"]/div/button/span