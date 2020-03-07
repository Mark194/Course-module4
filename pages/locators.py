from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[contains(@class,'btn btn-lg btn-primary btn-add-to-basket')]")
    COST_BASKET = (By.XPATH, "//div[contains(@class, 'basket-mini pull-right hidden-xs')]")
    COST_PRODUCT = (By.XPATH, "//p[contains(@class, 'price_color')]")
