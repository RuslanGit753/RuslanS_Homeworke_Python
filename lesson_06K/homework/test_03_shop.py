import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from form_locatos import ShopLoc


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture(scope="module", autouse=True)
def oper_form(wait):
    wait.until(EC.visibility_of_element_located(
        ShopLoc.name)).send_keys('standard_user')
    wait.until(EC.visibility_of_element_located(
        ShopLoc.password)).send_keys('secret_sauce')
    wait.until(EC.visibility_of_element_located(
        ShopLoc.login_button)).click()
    wait.until(EC.visibility_of_element_located(
        ShopLoc.add_backpack)).click()
    wait.until(EC.visibility_of_element_located(
        ShopLoc.add_bolt_shirt)).click()
    wait.until(EC.visibility_of_element_located(
        ShopLoc.add_labs_onesie)).click()
    wait.until(EC.visibility_of_element_located(
        ShopLoc.shopping)).click()
    wait.until(EC.visibility_of_element_located(
        ShopLoc.checkout_button)).click()
    wait.until(EC.visibility_of_element_located(
        ShopLoc.first_name)).send_keys('Ruslan')
    wait.until(EC.visibility_of_element_located(
        ShopLoc.last_name)).send_keys('Serebryakov')
    wait.until(EC.visibility_of_element_located(
        ShopLoc.index)).send_keys('757345')
    wait.until(EC.visibility_of_element_located(
        ShopLoc.continue_button)).click()


def test_summary_total(wait):
    summary_total = wait.until(EC.visibility_of_element_located(
        ShopLoc.summary_total)).text
    assert summary_total == 'Total: $58.29'
