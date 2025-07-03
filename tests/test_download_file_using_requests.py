from pages.saby_download_page import SabyDownloadPage
from pages.saby_main_page import SabyMainPage
from test_data.data import TestData


def test_download_plugin(browser):
    """Загрузка файла осуществляет при помощи с помощью библиотеки requests"""
    page_saby_main = SabyMainPage(browser, TestData.LINK_SABY)
    page_saby_main.open()
    page_saby_main.go_to_download_page()
    page_download = SabyDownloadPage(browser, browser.current_url)
    page_download.download_file_using_requests(TestData.FILE_NAME)
    page_download.should_be_file(TestData.FILE_NAME)
    page_download.should_be_correct_file_size(TestData.FILE_NAME)
    page_download.delete_file(TestData.FILE_NAME)