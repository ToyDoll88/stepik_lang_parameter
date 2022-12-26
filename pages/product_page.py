import math
from pages.base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def name_before(self):
        book_name_element = self.browser.find_element(*ProductPageLocators.BOOK_NAME_TO_ADD)
        return book_name_element.text

    def name_after(self):
        book_name_element = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED)
        return book_name_element.text

    def price_before(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_BEFORE)
        return price.text

    def price_after(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_AFTER)
        return price.text

    def add_to_cart(self):
        add_to_cart_button = \
            self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
