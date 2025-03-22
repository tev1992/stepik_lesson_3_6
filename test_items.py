import pytest
import time
from selenium.webdriver.common.by import By

def test_items(browser):
    link = 'http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/'
    browser.get(link)
    # time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').is_displayed(), 'Кнопка не найдена на странице'
