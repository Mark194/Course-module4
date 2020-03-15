from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
import faker

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
based_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
urls = [f"{based_link}{str(i)}" for i in range(10)]
urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)


@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        fake = faker.Faker()
        login_page.register_now(fake.email(), fake.password())
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, based_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, based_link)
        page.open()
        page.should_be_button_add_to_basket()
        page.add_to_basket()
        page.should_be_cost_equal()
        page.should_be_name_equal()


@pytest.mark.need_review
@pytest.mark.parametrize('url', urls)
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_to_basket()
    page.should_be_cost_equal()
    page.should_be_name_equal()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, based_link)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, based_link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, based_link)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_to_basket()
    page.should_not_be_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_item_in_basket()
    basket_page.should_be_basket_is_empty()
