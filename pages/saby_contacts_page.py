from .base_page import BasePage

from locators import SabyContactsLocators


class ContactsPage(BasePage):
    def go_to_tensor_page(self):
        self.browser.find_element(*SabyContactsLocators.TENSOR_PAGE).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
