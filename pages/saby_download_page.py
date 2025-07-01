import os

import requests

from locators import TensorDownloadLocators
from .base_page import BasePage


class SabyDownloadPage(BasePage):
    def get_download_link(self):
        link_download = self.browser.find_element(*TensorDownloadLocators.DOWNLOAD_PLUGIN)
        return link_download.get_attribute('href')

    def download_file(self, filename):
        download_link = self.get_download_link()
        response = requests.get(download_link)
        response.raise_for_status()
        with open(f'{filename}', 'wb') as file:
            file.write(response.content)

    @staticmethod
    def should_be_file(filename):
        files = os.listdir(".")
        assert filename in files, "Файл отсутствует в текущей дирректории"

    def should_be_correct_file_size(self, filename):
        file_size = os.path.getsize(filename) / (1024 * 1024.0)
        link_download = self.browser.find_element(*TensorDownloadLocators.DOWNLOAD_PLUGIN)
        assert str(round(file_size, 2)) in link_download.text, "Размер файла не верный"
