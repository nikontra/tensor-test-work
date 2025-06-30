from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from .base_page import BasePage
from locators import SabyMainPageLocators


class SabyMainPage(BasePage):
    def go_to_contacts_page(self):
        menu_contacts = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(SabyMainPageLocators.MENU_CONTACTS)
        )
        menu_contacts.click()
        self.browser.find_element(*SabyMainPageLocators.CONTACTS_PAGE).click()

    def go_to_download_page(self):
        download = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(SabyMainPageLocators.DOWNLOAD)
        )
        download.click()
