from pages.product_page import ProductPage
import time
import pytest

based_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
urls = [f"{based_link}{str(i)}" for i in range(10)]


@pytest.mark.parametrize('url', urls)
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_to_basket()
    page.should_be_cost_equal()
    page.should_be_name_equal()
