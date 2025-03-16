from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Выбери локализацию тестов: "--language=en" or "--language=ru"')

@pytest.fixture(scope='class')
def browser(request):
    user_language = request.config.getoption('language')
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_language': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nЗакрытие браузера')
    browser.quit()
