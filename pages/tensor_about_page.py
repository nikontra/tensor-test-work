from .tensor_main_page import TensorMainPage
from locators import TensorAboutLocators

class TensorAboutPage(TensorMainPage):
    def should_be_link(self):
        assert self.browser.current_url == "https://tensor.ru/about"

    def should_be_images_of_equal_size(self):
        images = self.browser.find_elements(*TensorAboutLocators.IMAGES)
        list_size = [(i.get_attribute("width"), i.get_attribute("height")) for i in images]
        assert len(set(list_size)) == 1, "Фотографии в разделе 'Работаем' разного размера"
