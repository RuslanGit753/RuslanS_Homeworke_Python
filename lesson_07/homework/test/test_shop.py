from pages.shop_page import ShopPage


def test_summary_total(driver, wait):
    shop_page = ShopPage(driver)
    shop_page.login(wait)
    shop_page.add_items_to_cart(wait)
    shop_page.checkout(wait)
    summary_total = shop_page.get_summary_total(wait)
    assert summary_total == 'Total: $58.29'
