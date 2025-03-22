from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Выбери локализацию тестов: "--language=en" or "--language=ru"')
    parser.addoption('--browser_name', action='store', default="Chrome", help='Выбери браузер: "--browser_name=chrome" or "--browser_name=firefox"')

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')

    # Настройка браузера
    if browser_name == 'Chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'Firefox':
        options_firefox = OptionsFirefox()
        options_firefox.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("Выбери локализацию тестов: из ['es', 'en', 'fr', 'ru'] и выбранный браузер")
    yield browser
    print('\nЗакрытие браузера')
    browser.quit()