import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

LOG = logging.getLogger(__name__)
LOG_FILTER = {
    '': 'DEBUG',
    'selenium': 'INFO',
    'urllib3.connectionpool': 'WARNING',
    'selenium.webdriver': 'INFO',
}

app_formatter = logging.Formatter(
    '%(asctime)s.%(msecs)03d [ %(levelname)8s ] '
    '%(name)s.%(funcName)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

app_handler = logging.StreamHandler()
app_handler.setLevel(logging.DEBUG)
app_handler.setFormatter(app_formatter)
logging.getLogger('').addHandler(app_handler)

for name, level in LOG_FILTER.items():
    logging.getLogger(name).setLevel(level)


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    LOG.info('start browser')
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption('language')
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {
            'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    LOG.info('quit browser')
    browser.quit()
