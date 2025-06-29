from pages.saby_main_page import MainPage
from pages.tensor_main_page import TensorPage
from pages.saby_contacts_page import ContactsPage
from pages.tensor_about_page import TensorAboutPage

LINK_SABY = "https://saby.ru"


def test_about_foto_size(browser):
    page_saby_main = MainPage(browser, LINK_SABY)
    page_saby_main.open()
    page_saby_main.go_to_contacts_page()
    page_contacts = ContactsPage(browser, browser.current_url)
    page_contacts.go_to_tensor_page()
    page_tensor = TensorPage(browser, browser.current_url)
    page_tensor.should_be_element()
    page_tensor.go_to_about_page()
    page_about = TensorAboutPage(browser, browser.current_url)
    page_about.should_be_link()
    page_about.should_be_image_of_equal_size()
