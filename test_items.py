import pytest
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from conftest import language


class TestElementDisplayed():
    def test_items(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(5)
        try:
            button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
            if button.is_displayed():
                print("Кнопка отображается на странице.")
            else:
                print('Кнопка не отображается на странице')
        except NoSuchElementException:
            print('Кнопка не найдена')



