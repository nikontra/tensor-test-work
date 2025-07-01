from pages.saby_contacts_page import ContactsSabyPage
from pages.saby_main_page import SabyMainPage

LINK_SABY = "https://saby.ru"
LOCATION = "Костромская обл."
NEW_LOCATION = "Камчатский край"
NEW_LOCATION_EN = "kamchatskij-kraj"
PARTNERS = [
    "Saby - Кострома",
    "Консультант Кострома",
    "ИП Турчанинов В.В."
]

def test_edit_location(browser):
    page_saby_main = SabyMainPage(browser, LINK_SABY)
    page_saby_main.open()
    page_saby_main.go_to_contacts_page()
    page_contact = ContactsSabyPage(browser, browser.current_url)
    page_contact.should_be_region(LOCATION)
    page_contact.should_be_list_partners(PARTNERS)
    page_contact.edit_region()
    page_contact.should_be_edit_region(LOCATION, NEW_LOCATION)
    page_contact.should_be_edited_list_partners(PARTNERS)
    page_contact.should_be_correct_url(NEW_LOCATION_EN)
    page_contact.should_be_correct_title(NEW_LOCATION)
