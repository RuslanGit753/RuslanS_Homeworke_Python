import allure
from locators.form_locatos import ShopLoc
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    """Класс для работы с оформлением заказа."""

    @allure.step("Инициализация Chrome драйвера")
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")

    @allure.step("Авторизация")
    def login(self, wait):
        wait.until(EC.visibility_of_element_located(
            ShopLoc.name)).send_keys('standard_user')
        wait.until(EC.visibility_of_element_located(
            ShopLoc.password)).send_keys('secret_sauce')
        wait.until(EC.visibility_of_element_located(
            ShopLoc.login_button)).click()

    @allure.step("Добавление товара в корзину")
    def add_items_to_cart(self, wait):
        wait.until(EC.visibility_of_element_located(
            ShopLoc.add_backpack)).click()
        wait.until(EC.visibility_of_element_located(
            ShopLoc.add_bolt_shirt)).click()
        wait.until(EC.visibility_of_element_located(
            ShopLoc.add_labs_onesie)).click()
        wait.until(EC.visibility_of_element_located(
            ShopLoc.shopping)).click()

    @allure.step("Офоррмление покупки")
    def checkout(self, wait):
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

    @allure.step("Возвращение суммы товаров")
    def get_summary_total(self, wait):
        return wait.until(EC.visibility_of_element_located(
            ShopLoc.summary_total)).text
