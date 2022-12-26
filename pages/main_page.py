from pages.base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login = self.browser.find_element(*MainPageLocators.LOGIN_ELEMENT)
        login.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_ELEMENT
        ), "Login link is not presented"
