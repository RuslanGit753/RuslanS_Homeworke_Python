from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 5)
driver.get("https://the-internet.herokuapp.com/login")


username = wait.until(EC.visibility_of_element_located((
    By.XPATH, '//input[@name="username"]')))
username.send_keys('tomsmith')

password = wait.until(EC.visibility_of_element_located((
    By.XPATH, '//input[@name="password"]')))
password.send_keys('SuperSecretPassword!')

login = wait.until(EC.visibility_of_element_located((
    By.XPATH, '//button[@type="submit"]')))
login.click()

logged = wait.until(EC.visibility_of_element_located((
    By.XPATH, '//div[@id="flash"]')))

print(logged.text[:-1])

driver.quit()
