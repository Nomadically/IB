from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\\ib\\PycharmProjects\\ibProject\\chromedriver.exe")
driver.get("https://www.bop.gov/inmateloc/")
print(driver.title)
time.sleep(1) # Let the user actually see something!

# print(driver.page_source)

inmate_number = 41138018

element = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/input")
element.send_keys(inmate_number)
element.send_keys(Keys.RETURN)
time.sleep(1)

result = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[6]/td/a")

print(result.click())

facility_name = driver.find_element(By.CLASS_NAME, "send-address-title")
# facility_address_street = driver.find_element
# facility_address_city = driver.find_element
# facility_address_state = driver.find_element
# facility_address_zip = driver.find_element

print(
    facility_name
)