import urllib
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome("C:\\Users\\ib\\PycharmProjects\\ibProject\\chromedriver.exe")
driver.get("https://www.bop.gov/inmateloc/")
print("this is title", driver.title)
time.sleep(1) # Let the user actually see something!

# print(driver.page_source)

# inmate_number = 41138018
inmate_number = "14083026"

element = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/input")
element.send_keys(inmate_number)
element.send_keys(Keys.RETURN)
time.sleep(1)

result = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[6]/td/a").click()

html_doc = requests.get('https://www.bop.gov/locations/institutions/tha/#send_things')
soup = BeautifulSoup(html_doc.content, 'html.parser')

holding = []
#f = codecs.open('temptext.txt', encoding='utf-8',mode='w+')
for string in soup.strings:
    holding.append(string)

index = holding.index('INMATE NAME & REGISTER NUMBER')

print(index)

print(holding[364])

time.sleep(3)
# driver.quit()
