import allure
from pages.shop_page import ShopPage


@allure.feature("Тестирование онлайн-магазина")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест покупки товаров")
@allure.description("Тестирование процесса авторизации, "
                    "добавления товаров в корзину, "
                    "оформления заказа и проверки итоговой суммы заказа")
def test_summary_total(driver, wait):
    """Тест покупки товаров в интернет-магазине."""
    with allure.step("Открытие сайта онлайн-магазина"):
        shop_page = ShopPage(driver)

    with allure.step("Авторизация"):
        shop_page.login(wait)

    with allure.step("Добавление товара в корзину"):
        shop_page.add_items_to_cart(wait)

    with allure.step("Офоррмление покупки"):
        shop_page.checkout(wait)

    with allure.step("Проверки итоговой суммы заказа"):
        summary_total = shop_page.get_summary_total(wait)
        assert summary_total == 'Total: $58.29'
