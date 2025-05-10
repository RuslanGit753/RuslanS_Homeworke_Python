import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("http://uitestingplayground.com/dynamicid")


button = driver.find_element(
    By.XPATH, '//button[@class="btn btn-primary" and @type="button"]'
    )
button.click()

time.sleep(5)
