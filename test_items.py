from selenium.webdriver.common.by import By
import logging
from selenium.common.exceptions import NoSuchElementException

LOG = logging.getLogger(__name__)


def test_check_add_cart_button(browser):
    LOG.info('check title')
    browser.find_element(By.XPATH, './/h1[text()="Coders at Work"]')
    LOG.info('check availability')
    browser.find_element(By.XPATH, './/i[contains(@class, "icon-ok")]')
    LOG.info('check add-to-cart button')
    browser.implicitly_wait(3)
    # totally pointless and weird assertion there
    button = browser.find_elements(
        By.XPATH,
        './/button[contains(@class, "btn-add-to-basket")]'
    )
    assert len(button) > 0
