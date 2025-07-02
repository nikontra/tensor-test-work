from locators import TensorAboutLocators
from .tensor_main_page import TensorMainPage


class TensorAboutPage(TensorMainPage):
    """Класс методов для страницы 'О компании' сайта Tensor"""

    def should_be_images_of_equal_size(self):
        """Метод проверяет одинаковые ли размеры фотографий"""
        images = self.browser.find_elements(*TensorAboutLocators.IMAGES)
        list_size = [(i.get_attribute("width"), i.get_attribute("height")) for i in images]
        assert len(set(list_size)) == 1, "Фотографии в разделе 'Работаем' разного размера"
