from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import SabyContactsLocators
from .base_page import BasePage


class ContactsSabyPage(BasePage):
    """Класс методов для страницы контактов сайта Saby"""

    def get_list_partners(self):
        """Метод возвращает список партнеров"""
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(SabyContactsLocators.LIST_PARTNERS)
        )
        list_partners = self.browser.find_elements(*SabyContactsLocators.LIST_PARTNERS)
        return [i.text for i in list_partners]

    def go_to_tensor_page(self):
        """Метод осуществляет переход на страницу сайта Tensor"""
        self.browser.find_element(*SabyContactsLocators.TENSOR_PAGE).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def should_be_region(self, location):
        """Метод проверяет правильно ли определен регион"""
        region_name = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(SabyContactsLocators.REGION)
        )
        print(region_name.text)
        assert region_name.text == location, "Регион определен не верно"

    def should_be_edit_region(self, old_region, new_region):
        """Метод проверяет, изменился ли регион"""
        WebDriverWait(self.browser, 10).until_not(
            EC.text_to_be_present_in_element(SabyContactsLocators.REGION, old_region)
        )
        region = self.browser.find_element(*SabyContactsLocators.REGION)
        assert region.text == new_region, "Регион принял неверное значение"

    def should_be_list_partners(self, partners):
        """Метод проверяет, отображается ли список партнеров"""
        assert self.get_list_partners() == partners, "Список партнеров не корректен"

    def edit_region(self):
        """Метод изменяет регион"""
        self.browser.find_element(*SabyContactsLocators.REGION).click()
        new_region = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(SabyContactsLocators.NEW_REGION)
        )
        actions = ActionChains(self.browser)
        actions.move_to_element(new_region).perform()
        new_region.click()

    def should_be_edited_list_partners(self, partners):
        """Метод проверяет, изменился ли список партнеров"""
        assert self.get_list_partners() != partners, "Список партнеров не изменился"

    def should_be_correct_url(self, name_region):
        """Метод проверяет наличие названия региона в URL"""
        assert name_region in self.browser.current_url, "Название региона отсутствует в адресе страницы"

    def should_be_correct_title(self, name_region):
        """Метод проверяет наличие названия региона в заголовке страницы"""
        assert name_region in self.browser.title, "Название региона отсутствует в заголовке страницы"
