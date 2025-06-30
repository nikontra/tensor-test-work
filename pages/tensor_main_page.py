from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from locators import TensorMainLocators


NAME_BLOCK = "Сила в людях"

class TensorMainPage(BasePage):
    def should_be_element(self):
        strength_in_people = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(TensorMainLocators.STRENGTH_IN_PEOPLE)
        )
        assert strength_in_people.text == NAME_BLOCK, 'Блок "Сила в людях" не найден'

    def go_to_about_page(self):
        self.browser.find_element(*TensorMainLocators.ABOUT_PAGE).click()
