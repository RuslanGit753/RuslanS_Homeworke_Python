import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from form_locatos import CalcLoc


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def wait(driver):
    return WebDriverWait(driver, 45)


@pytest.fixture(scope="module", autouse=True)
def input_num(wait):
    wait.until(EC.visibility_of_element_located(
        CalcLoc.input_num)).clear()
    wait.until(EC.visibility_of_element_located(
        CalcLoc.input_num)).send_keys('45')
    wait.until(EC.visibility_of_element_located(
        CalcLoc.num_7)).click()
    wait.until(EC.visibility_of_element_located(
        CalcLoc.oper_plus)).click()
    wait.until(EC.visibility_of_element_located(
        CalcLoc.num_8)).click()
    wait.until(EC.visibility_of_element_located(
        CalcLoc.oper_equally)).click()


def test_result(wait):
    wait.until(EC.text_to_be_present_in_element(CalcLoc.result, '15'))
    result = wait.until(EC.visibility_of_element_located(
        CalcLoc.result)).text
    assert result == '15'
