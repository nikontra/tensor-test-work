from pages.saby_download_page import SabyDownloadPage
from pages.saby_main_page import SabyMainPage

LINK_SABY = "https://saby.ru"
FILE_NAME = "plugin.exe"

def test_download_plugin(browser):
    page_saby_main = SabyMainPage(browser, LINK_SABY)
    page_saby_main.open()
    page_saby_main.go_to_download_page()
    page_download = SabyDownloadPage(browser, browser.current_url)
    page_download.download_file(FILE_NAME)
    page_download.should_be_file(FILE_NAME)
    page_download.should_be_correct_file_size(FILE_NAME)
    # time.sleep(5)
