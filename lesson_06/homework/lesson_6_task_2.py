from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://uitestingplayground.com/textinput")
wait = WebDriverWait(driver, 5)

input_text = wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '.form-control'))).send_keys('SkyPro')

button = wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '#updatingButton'))).click()

button_text = wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '#updatingButton'))).text

print(button_text)
