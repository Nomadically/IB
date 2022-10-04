import urllib
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class DemoHiddenElements():
    def demo_is_displayed(self):
        driver = webdriver.Chrome("C:\\Users\\ib\\PycharmProjects\\ibProject\\chromedriver.exe")
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        present = driver.find_element(By.XPATH, '//*[@id="myDIV"]').is_displayed()
        print(present)
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        present1 = driver.find_element(By.XPATH, '//*[@id="myDIV"]').is_displayed()
        time.sleep(3)
        print(present1)
        time.sleep(5)

    def demo_is_not_displayed(self):
        driver = webdriver.Chrome("C:\\Users\\ib\\PycharmProjects\\ibProject\\chromedriver.exe")
        # driver.get("https://www.yatra.com/hotels")
        # driver.find_element(By.XPATH, "//label[normalize-space()='Traveller and Hotel']").click()
        # driver.get("https://www.bop.gov/locations/institutions/tha/") #works for this
        driver.get("https://www.bop.gov/locations/institutions/ali/")
        driver.find_element(By.XPATH, "//a[normalize-space()='Inmate Mail']").click()
        time.sleep(2)
        # driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[2]").click()
        elem0 = driver.find_element(By.XPATH, "//div[@id='send_address_inmate']//div[@class='address-item']//span[1]")
        # elem1 = driver.find_element(By.XPATH, "(//span[@class='send-address-title'][normalize-space()='FCI Terre Haute'])[1]")
        elem1 = driver.find_element(By.XPATH, "//span[@class='send-address-title']")
        elem2 = driver.find_element(By.XPATH, "//span[@class='send-address-desc']")
        elem3 = driver.find_element(By.XPATH, "//span[@class='send-address-street']")
        elem4 = driver.find_element(By.XPATH, "//span[@class='send-address-city']")
        elem5 = driver.find_element(By.XPATH, "//span[@class='send-address-state']")
        elem6 = driver.find_element(By.XPATH, "//span[@class='send-address-zip']")
        time.sleep(2)
        print(elem0.is_displayed())
        print(f"Facility name: {elem1.text} and {elem2.text}.\n Street:{elem3.text}.\n City:{elem4.text}"
              f"State:{elem5.text}. \n Zipcode: {elem6.text}.")
        # elem = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        # print(elem)
        # driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]").click()
        # elem1 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        # print(elem1)


demo = DemoHiddenElements()
demo.demo_is_not_displayed()
# demo.demo_is_displayed()



# https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp


"""









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

def finding():
    result = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[6]/td/a").click()
    # fac_name = driver.find_element_by_class_name("send-address-title")
    # click_here_link = driver.find_element_by_link_text('Click Here')
    time.sleep(1)
    fac_name = driver.find_element(By.PARTIAL_LINK_TEXT, "How to send things here").click()
    # print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.current-stage"))).text)
    # result2 = fac_name.getText()
    time.sleep(1)
    # print(fac_name)
    print(
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Inmate Mail"))).text)


finding()
"""
"""
Older code that attempted to use soup =



html_doc = requests.get('https://www.bop.gov/locations/institutions/tha/#send_things')
soup = BeautifulSoup(html_doc.content, 'html.parser')

print(soup.title.text)


holding = []
#f = codecs.open('temptext.txt', encoding='utf-8',mode='w+')
for string in soup.strings:
    holding.append(string)

index = holding.index('INMATE NAME & REGISTER NUMBER')

print(index)

print(holding)

time.sleep(1)
# driver.quit()


"""
