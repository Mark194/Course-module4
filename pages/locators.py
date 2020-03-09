from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_INPUT = (By.XPATH, "//input[@id='id_registration-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='id_registration-password1']")
    PASSWORD_REPEAT_INPUT = (By.XPATH, "//input[@id='id_registration-password2']")
    BUTTON_REGISTER = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[contains(@class,'btn btn-lg btn-primary btn-add-to-basket')]")
    COST_BASKET = (By.XPATH, "//div[contains(@class, 'basket-mini pull-right hidden-xs')]")
    COST_PRODUCT = (By.XPATH, "//p[contains(@class, 'price_color')]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_ABOUT_ADD = (By.XPATH, "//div[@class='alertinner ']/strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    NO_ITEM = (By.XPATH, "//div[@class='basket-title hidden-xs']")
    BASKET_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")
