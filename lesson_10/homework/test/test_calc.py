import allure
from pages.calc_page import CalcPage


@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест вычисления суммы")
@allure.description("Тестирование работы калькулятора с операцией сложения.")
def test_result(driver, wait):
    """Функция вычисления 7 + 8"""

    with allure.step("Инициализация калькулятора"):
        calc_page = CalcPage(driver)

    with allure.step("Установка задержки"):
        calc_page.input_num(wait)

    with allure.step("Ввод данных для вычисления"):
        calc_page.summ_num(wait)

    with allure.step("Получение и проверка результата"):
        result = calc_page.result_num(wait)
        assert result == "15"
