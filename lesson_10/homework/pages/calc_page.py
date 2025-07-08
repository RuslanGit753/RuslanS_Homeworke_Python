import allure
from locators.form_locatos import CalcLoc
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    """Класс для работы с калькулятором на странице."""

    @allure.step("Инициализация Chrome драйвера")
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver"
            "-java/slow-calculator.html")

    @allure.step("Ввод времени ожидания результата вычеслений")
    def input_num(self, wait):
        wait.until(EC.visibility_of_element_located(
            CalcLoc.input_num)).clear()
        wait.until(EC.visibility_of_element_located(
            CalcLoc.input_num)).send_keys('45')

    @allure.step("Ввод данных для вычесления суммы")
    def summ_num(self, wait):
        wait.until(EC.visibility_of_element_located(
            CalcLoc.num_7)).click()
        wait.until(EC.visibility_of_element_located(
            CalcLoc.oper_plus)).click()
        wait.until(EC.visibility_of_element_located(
            CalcLoc.num_8)).click()
        wait.until(EC.visibility_of_element_located(
            CalcLoc.oper_equally)).click()

    @allure.step("Ожидание появления результата")
    def result_num(self, wait):
        wait.until(EC.text_to_be_present_in_element(CalcLoc.result, '15'))
        return wait.until(EC.visibility_of_element_located(
            CalcLoc.result)).text
