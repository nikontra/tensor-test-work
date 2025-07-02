from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import TensorMainLocators
from .base_page import BasePage


class TensorMainPage(BasePage):
    """Класс методов для главной страницы сайта Tensor"""

    def should_be_element(self, name_block):
        """Метод проверяет наличие блока 'Сила в людях'"""
        strength_in_people = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(TensorMainLocators.STRENGTH_IN_PEOPLE)
        )
        assert strength_in_people.text == name_block, 'Блок "Сила в людях" не найден'

    def go_to_about_page(self):
        """Метод осуществляет переход на страницу 'О компании' сайта Tensor"""
        self.browser.find_element(*TensorMainLocators.ABOUT_PAGE).click()
