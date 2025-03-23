from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Выбери локализацию тестов: "--language"')
    parser.addoption('--browser_name', action='store', default='Chrome', help='Выбери браузер: "--browser_name=chrome" or "--browser_name=firefox"')

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    # Проверка, что язык указан при запуске тестов
    if user_language is None:
        raise pytest.UsageError("Выбери локализацию тестов, пример: ['--language=es', '--language=en', '--language=fr', '--language=ru']")
    # Настройка браузера
    if browser_name == 'Chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'Firefox':
        options_firefox = OptionsFirefox()
        options_firefox.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options_firefox)
    # Проверка, если браузер не задан, по умолчанию открывается 'Chrome'
    else:
        raise pytest.UsageError("выбери браузер: 'Сhrome' или 'Firefox'")
    yield browser
    print('\nЗакрытие браузера')
    browser.quit()