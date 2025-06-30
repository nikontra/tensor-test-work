import time

from pages.saby_main_page import SabyMainPage
from pages.saby_contacts_page import ContactsSabyPage


LINK_SABY = "https://saby.ru"
LOCATION = "Костромская обл."
NEW_LOCATION = "Камчатский край"

def test_edit_location(browser):
    page_saby_main = SabyMainPage(browser, LINK_SABY)
    page_saby_main.open()
    page_saby_main.go_to_contacts_page()
    page_contact = ContactsSabyPage(browser, browser.current_url)
    page_contact.should_be_region(LOCATION)
    page_contact.should_be_list_partners()
    page_contact.edit_region()
    page_contact.should_be_region(NEW_LOCATION)