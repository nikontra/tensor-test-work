import logging

from pages.saby_contacts_page import ContactsSabyPage
from pages.saby_main_page import SabyMainPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_main_page import TensorMainPage
from test_data.data import TestData

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()


def test_about_foto_size(browser):
    """Тест на сравнение размера фото на странице 'О компании'"""
    mylogger.info('Start test foto size')
    page_saby_main = SabyMainPage(browser, TestData.LINK_SABY)
    page_saby_main.open()
    page_saby_main.go_to_contacts_page()
    page_contacts = ContactsSabyPage(browser, browser.current_url)
    page_contacts.go_to_tensor_page()
    page_tensor = TensorMainPage(browser, browser.current_url)
    page_tensor.should_be_element(TestData.NAME_BLOCK_IN_TENSOR)
    page_tensor.go_to_about_page()
    page_about = TensorAboutPage(browser, browser.current_url)
    page_about.should_be_link(TestData.LINK_TENSOR_ABOUT)
    page_about.should_be_images_of_equal_size()
    mylogger.info('End test foto size')

