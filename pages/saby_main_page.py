from .base_page import BasePage
from locators import SabyMainPageLocators


class SabyMainPage(BasePage):
    def go_to_contacts_page(self):
        self.browser.find_element(*SabyMainPageLocators.MENU_CONTACTS).click()
        self.browser.find_element(*SabyMainPageLocators.CONTACTS_PAGE).click()
