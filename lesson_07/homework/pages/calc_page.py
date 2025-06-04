from selenium.webdriver.support import expected_conditions as EC

from locators.form_locatos import CalcLoc


class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver"
            "-java/slow-calculator.html")

    def input_num(self, wait):
        wait.until(EC.visibility_of_element_located(
            CalcLoc.input_num)).clear()
        wait.until(EC.visibility_of_element_located(
            CalcLoc.input_num)).send_keys('45')

    def summ_num(self, wait):
        wait.until(EC.visibility_of_element_located(
            CalcLoc.num_7)).click()
        wait.until(EC.visibility_of_element_located(
            CalcLoc.oper_plus)).click()
        wait.until(EC.visibility_of_element_located(
            CalcLoc.num_8)).click()
        wait.until(EC.visibility_of_element_located(
            CalcLoc.oper_equally)).click()

    def result_num(self, wait):
        wait.until(EC.text_to_be_present_in_element(CalcLoc.result, '15'))
        return wait.until(EC.visibility_of_element_located(
            CalcLoc.result)).text
