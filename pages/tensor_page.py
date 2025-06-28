from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class TensorPage(BasePage):
    def should_be_element(self):
        strength_in_people = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p:nth-child(1)"))
        )
        assert strength_in_people.text == "Сила в людях"

    def go_to_about_page(self):
        self.browser.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p:nth-child(4) a").click()

