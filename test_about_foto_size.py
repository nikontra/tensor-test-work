import time

import pytest
import selenium
from selenium.webdriver.common.by import By


def test_about_foto_size(browser):
    browser.get("https://saby.ru")
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, ".sbisru-Header ul li:nth-child(2)").click()
    time.sleep(1)
    office = browser.find_element(By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu__items .sbisru-link")
    time.sleep(1)
    office.click()
    time.sleep(1)
    tensor = browser.find_element(By.CSS_SELECTOR, "#contacts_clients .sbisru-Contacts__border-left a")
    time.sleep(1)
    link_tensor = tensor.get_attribute("href")
    time.sleep(1)
    browser.get(link_tensor)
    strength_in_people = browser.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p:nth-child(1)")
    time.sleep(4)
    assert strength_in_people.text == "Сила в людях"
    more_detail = browser.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p:nth-child(4) a")
    link_detail = more_detail.get_attribute("href")
    time.sleep(1)
    browser.get(link_detail)
    assert "about" in browser.current_url
    time.sleep(2)
    images = browser.find_elements(By.CSS_SELECTOR, ".tensor_ru-About__block3 img")
    list_size = []
    for i in images:
        list_size.append((i.get_attribute("width"), i.get_attribute("height")))
    assert len(set(list_size)) == 1






