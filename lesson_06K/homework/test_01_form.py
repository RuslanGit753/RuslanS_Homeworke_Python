import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from form_locatos import InputLoc, ColorLoc


BACK_GREEN = 'rgba(209, 231, 221, 1)'
BACK_RED = 'rgba(248, 215, 218, 1)'


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture(scope="module", autouse=True)
def fill_form(wait):
    wait.until(EC.visibility_of_element_located(
        InputLoc.first_name)).send_keys('Иван')
    wait.until(EC.visibility_of_element_located(
        InputLoc.last_name)).send_keys('Петров')
    wait.until(EC.visibility_of_element_located(
        InputLoc.address)).send_keys('Ленина, 55-3')
    wait.until(EC.visibility_of_element_located(
        InputLoc.mail)).send_keys('test@skypro.com')
    wait.until(EC.visibility_of_element_located(
        InputLoc.phone)).send_keys('+7985899998787')
    wait.until(EC.visibility_of_element_located(
        InputLoc.city)).send_keys('Москва')
    wait.until(EC.visibility_of_element_located(
        InputLoc.country)).send_keys('Россия')
    wait.until(EC.visibility_of_element_located(
        InputLoc.position)).send_keys('QA')
    wait.until(EC.visibility_of_element_located(
        InputLoc.company)).send_keys('SkyPro')
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@type="submit"]'))).click()


def test_back_first(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.first_name))
    assert element.value_of_css_property(
        'background-color') == BACK_GREEN


def test_back_last(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.last_name))
    assert element.value_of_css_property(
        'background-color') == BACK_GREEN


def test_back_address(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.address))
    assert element.value_of_css_property(
        'background-color') == BACK_GREEN


def test_back_mail(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.mail))
    assert element.value_of_css_property(
        'background-color') == BACK_GREEN


def test_back_phone(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.phone))
    assert element.value_of_css_property(
        'background-color') == BACK_GREEN


def test_back_city(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.city))
    assert element.value_of_css_property(
        'background-color') == BACK_GREEN


def test_back_country(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.country))
    assert element.value_of_css_property(
        'background-color') == BACK_GREEN


def test_back_position(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.position))
    assert element.value_of_css_property(
        'background-color') == BACK_GREEN


def test_back_company(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.company))
    assert element.value_of_css_property(
        'background-color') == BACK_GREEN


def test_back_code(wait):
    element = wait.until(EC.visibility_of_element_located(
        ColorLoc.code))
    assert element.value_of_css_property(
        'background-color') == BACK_RED
