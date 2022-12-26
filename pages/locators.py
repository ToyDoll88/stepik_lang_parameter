from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_ELEMENT = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART = (
        By.XPATH,
        './/button[contains(@class, "btn-lg btn-primary")]'
    )
    BOOK_NAME_TO_ADD = (By.XPATH, './/div[@class="col-sm-6 product_main"]/h1')
    BOOK_NAME_ADDED = (By.XPATH, './/div[contains(@class, "alert-succes")][1]/div[@class="alertinner "]/strong')
    PRICE_BEFORE = (By.XPATH, './/p[@class="price_color"]')
    PRICE_AFTER = (By.XPATH, './/div[@class="alertinner "]/p/strong')