from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NO_ITEM), "Basket have item"

    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is not empty"
