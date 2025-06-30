from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains

from .base_page import BasePage
from locators import SabyContactsLocators


PARTNERS = [
    "Saby - Кострома",
    "Консультант Кострома",
    "ИП Турчанинов В.В."
]



class ContactsSabyPage(BasePage):
    def go_to_tensor_page(self):
        self.browser.find_element(*SabyContactsLocators.TENSOR_PAGE).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def should_be_region(self, location):
        # region_name = self.browser.find_element(*SabyContactsLocators.REGION)
        region_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(SabyContactsLocators.REGION)
        )
        assert region_name.text == location, "Регион определен не верно"

    def should_be_list_partners(self):
        list_partners = self.browser.find_elements(*SabyContactsLocators.LIST_PARTNERS)
        for i in list_partners:
            assert i.text in PARTNERS, f'"{i.text}" отсутствует в списке партнеров'

    def edit_region(self):
        self.browser.find_element(*SabyContactsLocators.REGION).click()
        new_region = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SabyContactsLocators.NEW_REGION)
        )
        actions = ActionChains(self.browser)
        actions.move_to_element(new_region).perform()
        new_region.click()

    # def should_be_new_region(self, location):
    #     region_name = self.browser.find_element(*SabyContactsLocators.REGION)
    #     assert region_name.text == location, "Регион определен не верно"
