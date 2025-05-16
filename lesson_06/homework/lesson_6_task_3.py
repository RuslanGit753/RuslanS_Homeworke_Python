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
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait = WebDriverWait(driver, 10)

img1 = wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '#compass')))

img2 = wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '#calendar')))

img3 = wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '#award'))).get_dom_attribute('src')

img4 = wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '#landscape')))

print(img3)
