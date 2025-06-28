import pytest
import selenium
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from pages.tensor_page import TensorPage

LINK_SABY = "https://saby.ru"










def should_be_link(browser):
    assert browser.current_url == "https://tensor.ru/about"


def should_be_image_of_equal_size(browser):
    images = browser.find_elements(By.CSS_SELECTOR, ".tensor_ru-About__block3 img")
    list_size = [(i.get_attribute("width"), i.get_attribute("height")) for i in images]
    assert len(set(list_size)) == 1



def test_about_foto_size(browser):
    page_saby = MainPage(browser, LINK_SABY)
    page_saby.open()
    page_saby.go_to_contacts_page()
    page_saby.go_to_tensor_page()
    page_tensor = TensorPage(browser, browser.current_url)
    page_tensor.should_be_element()
    page_tensor.go_to_about_page()
    should_be_link(browser)
    should_be_image_of_equal_size(browser)
