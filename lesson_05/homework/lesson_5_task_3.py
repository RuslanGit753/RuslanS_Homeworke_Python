import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("https://the-internet.herokuapp.com/inputs")


input_text = driver.find_element(By.XPATH, '//input[@type="number"]')
input_text.send_keys('Sky')
time.sleep(2)
input_text.clear()
time.sleep(2)
input_text.send_keys('Pro')
time.sleep(2)
driver.quit()
