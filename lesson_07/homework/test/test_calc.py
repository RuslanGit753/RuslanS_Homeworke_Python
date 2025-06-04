from pages.calc_page import CalcPage


def test_result(driver, wait):
    calc_page = CalcPage(driver)
    calc_page.input_num(wait)
    calc_page.summ_num(wait)
    result = calc_page.result_num(wait)
    assert result == "15"
