from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

language = ["en", "fr", "es", "ru"]

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Выбери локализацию тестов: "--language=en" or "--language=ru"')

@pytest.fixture(params=language)
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_language': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nЗакрытие браузера')
    browser.quit()
