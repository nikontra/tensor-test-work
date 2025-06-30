from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from .base_page import BasePage
from locators import SabyContactsLocators


class ContactsSabyPage(BasePage):
    def get_list_partners(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(SabyContactsLocators.LIST_PARTNERS)
        )
        list_partners = self.browser.find_elements(*SabyContactsLocators.LIST_PARTNERS)
        return [i.text for i in list_partners]

    def go_to_tensor_page(self):
        self.browser.find_element(*SabyContactsLocators.TENSOR_PAGE).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def should_be_region(self, location):
        region_name = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(SabyContactsLocators.REGION)
        )
        assert region_name.text == location, "Регион определен не верно"

    def should_be_list_partners(self, partners):
        assert self.get_list_partners() == partners, "Список партнеров не корректен"

    def edit_region(self):
        self.browser.find_element(*SabyContactsLocators.REGION).click()
        new_region = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(SabyContactsLocators.NEW_REGION)
        )
        actions = ActionChains(self.browser)
        actions.move_to_element(new_region).perform()
        new_region.click()

    def should_be_edited_list_partners(self, partners):
        assert self.get_list_partners() != partners, "Список партнеров не изменился"

    def should_be_correct_url(self, name_region):
        assert name_region in self.browser.current_url, "Название региона отсутствует в адресе страницы"

    def should_be_correct_title(self, name_region):
        assert name_region in self.browser.title, "Название региона отсутствует в заголовке страницы"
