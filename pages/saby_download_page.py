import logging
import os

import requests
from selenium.webdriver.support.wait import WebDriverWait

from locators import TensorDownloadLocators
from .base_page import BasePage

mylogger = logging.getLogger(__name__)


class SabyDownloadPage(BasePage):
    """Класс методов для станицы 'Скачать' сайта Saby"""

    def download_file_using_requests(self, filename):
        """Метод загружает файл через библиотеку requests"""
        download_link = self.get_link(TensorDownloadLocators.DOWNLOAD_PLUGIN)
        response = requests.get(download_link)
        response.raise_for_status()
        with open(f'{filename}', 'wb') as file:
            file.write(response.content)
        mylogger.info("File downloaded successfully")

    def download_file_by_click(self, filename):
        """Метод загружает файл через браузер"""
        self.browser.find_element(*TensorDownloadLocators.DOWNLOAD_PLUGIN).click()
        WebDriverWait(self.browser, 10).until(lambda _: filename in os.listdir("."))
        mylogger.info("File downloaded successfully")

    @staticmethod
    def should_be_file(filename):
        """Метод проверяет наличие скачанного файла в директории"""
        files = os.listdir(".")
        assert filename in files, "Файл отсутствует в текущей дирректории"

    def should_be_correct_file_size(self, filename):
        """Метод проверяет размер файла"""
        file_size = os.path.getsize(filename) / (1024 * 1024.0)
        link_download = self.browser.find_element(*TensorDownloadLocators.DOWNLOAD_PLUGIN)
        assert str(round(file_size, 2)) in link_download.text, "Размер файла не верный"

    @staticmethod
    def delete_file(filename):
        """Метод удаляет файл"""
        try:
            os.remove(filename)
        except OSError:
            mylogger.info("Файл не найден")
        mylogger.info("File successfully deleted")
