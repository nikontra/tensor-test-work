from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import SabyMainPageLocators
from .base_page import BasePage


class SabyMainPage(BasePage):
    """Класс методов для главной страницы сайта Saby"""

    def go_to_contacts_page(self):
        """Метод осуществляет переход на страницу 'Контакты' сайта Saby"""
        menu_contacts = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(SabyMainPageLocators.MENU_CONTACTS)
        )
        menu_contacts.click()
        self.browser.find_element(*SabyMainPageLocators.CONTACTS_PAGE).click()

    def go_to_download_page(self):
        """Метод осуществляет переход на страницу 'Скачать' сайта Saby"""
        download = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(SabyMainPageLocators.DOWNLOAD)
        )
        download.click()
