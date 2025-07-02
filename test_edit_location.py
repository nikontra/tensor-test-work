from pages.saby_contacts_page import ContactsSabyPage
from pages.saby_main_page import SabyMainPage
from test_data.data import TestData


def test_edit_location(browser):
    """Тест на изменение региона"""
    page_saby_main = SabyMainPage(browser, TestData.LINK_SABY)
    page_saby_main.open()
    page_saby_main.go_to_contacts_page()
    page_contact = ContactsSabyPage(browser, browser.current_url)
    page_contact.should_be_region(TestData.LOCATION)
    page_contact.should_be_list_partners(TestData.PARTNERS)
    page_contact.edit_region()
    page_contact.should_be_edit_region(TestData.LOCATION, TestData.NEW_LOCATION)
    page_contact.should_be_edited_list_partners(TestData.PARTNERS)
    page_contact.should_be_correct_url(TestData.NEW_LOCATION_EN)
    page_contact.should_be_correct_title(TestData.NEW_LOCATION)
