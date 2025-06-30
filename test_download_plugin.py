import time

from pages.saby_main_page import SabyMainPage
from pages.saby_download_page import SabyDownloadPage

LINK_SABY = "https://saby.ru"

def test_download_plugin(browser):
    page_saby_main = SabyMainPage(browser, LINK_SABY)
    page_saby_main.open()
    page_saby_main.go_to_download_page()
    page_download = SabyDownloadPage(browser, browser.current_url)
    
    time.sleep(3)
    