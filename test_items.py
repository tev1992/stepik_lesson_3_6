import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def test_add_to_card_button_id_displayed(browser):
    link = 'http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    try:
        button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    except NoSuchElementException:
        assert False, 'Кнопка не найдена на странице'

