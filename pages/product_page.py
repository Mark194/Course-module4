from selenium.common.exceptions import NoAlertPresentException # в начале файла
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_add_to_basket(self):
        self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET)

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_cost_equal(self):
        cost_basket = self.browser.find_element(*ProductPageLocators.COST_BASKET).text
        cost_item = self.browser.find_element(*ProductPageLocators.COST_PRODUCT).text
        assert cost_item in cost_basket, "Cost in basket and in item not equal"

