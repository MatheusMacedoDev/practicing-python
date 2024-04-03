from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")

title = driver.title
print(title)

copy = driver.find_element(By.CSS_SELECTOR, 'div.slide-copy').text
print(copy)

donate_button = driver.find_element(By.CSS_SELECTOR, 'a.donate-button')
donate_button.click()

driver.close()