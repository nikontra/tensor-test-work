import logging

from pages.saby_download_page import SabyDownloadPage
from pages.saby_main_page import SabyMainPage
from test_data.data import TestData

mylogger = logging.getLogger(__name__)


def test_download_plugin(browser):
    """Загрузка файла осуществляется кликом по ссылке.
    В конце теста происходит удаление загруженного файла.
    Если удаление не требуется, необходимо закоментить предпоследнюю строку теста."""
    mylogger.info("Start test download file")
    page_saby_main = SabyMainPage(browser, TestData.LINK_SABY)
    page_saby_main.open()
    page_saby_main.go_to_download_page()
    page_download = SabyDownloadPage(browser, browser.current_url)
    page_download.download_file_by_click(TestData.FILE_NAME)
    page_download.should_be_file(TestData.FILE_NAME)
    page_download.should_be_correct_file_size(TestData.FILE_NAME)
    page_download.delete_file(TestData.FILE_NAME)
    mylogger.info("End test download file")
