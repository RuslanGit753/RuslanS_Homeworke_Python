from selenium.webdriver.common.by import By


class CalcLoc:
    """Класс для записи локаторов со страницы калькуляторв"""
    input_num = (By.CSS_SELECTOR, '#delay')
    num_7 = (By.XPATH, "//span[text()='7']")
    num_8 = (By.XPATH, "//span[text()='8']")
    oper_plus = (By.XPATH, "//span[text()='+']")
    oper_equally = (By.XPATH, "//span[text()='=']")
    result = (By.XPATH, '//div[@class="screen"]')


class ShopLoc:
    """Класс для записи локаторов со страницы магазина"""
    name = (By.CSS_SELECTOR, '#user-name')
    password = (By.CSS_SELECTOR, '#password')
    login_button = (By.CSS_SELECTOR, '#login-button')
    add_backpack = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    add_bolt_shirt = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    add_labs_onesie = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
    shopping = (By.CSS_SELECTOR, '.shopping_cart_link')
    checkout_button = (By.CSS_SELECTOR, '#checkout')
    first_name = (By.CSS_SELECTOR, '#first-name')
    last_name = (By.CSS_SELECTOR, '#last-name')
    index = (By.CSS_SELECTOR, '#postal-code')
    continue_button = (By.CSS_SELECTOR, '#continue')
    summary_total = (By.CSS_SELECTOR, '.summary_total_label')
