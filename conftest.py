import pytest
import logging
from selenium import webdriver

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


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
    LOG.info('start browser')
    browser.get(link)
    yield browser
    LOG.info('quit browser')
    browser.quit()
