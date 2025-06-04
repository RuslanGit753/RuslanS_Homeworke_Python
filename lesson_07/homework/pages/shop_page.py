from selenium.webdriver.support import expected_conditions as EC

from locators.form_locatos import ShopLoc


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")

    def login(self, wait):
        wait.until(EC.visibility_of_element_located(
            ShopLoc.name)).send_keys('standard_user')
        wait.until(EC.visibility_of_element_located(
            ShopLoc.password)).send_keys('secret_sauce')
        wait.until(EC.visibility_of_element_located(
            ShopLoc.login_button)).click()

    def add_items_to_cart(self, wait):
        wait.until(EC.visibility_of_element_located(
            ShopLoc.add_backpack)).click()
        wait.until(EC.visibility_of_element_located(
            ShopLoc.add_bolt_shirt)).click()
        wait.until(EC.visibility_of_element_located(
            ShopLoc.add_labs_onesie)).click()
        wait.until(EC.visibility_of_element_located(
            ShopLoc.shopping)).click()

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

    def get_summary_total(self, wait):
        return wait.until(EC.visibility_of_element_located(
            ShopLoc.summary_total)).text
