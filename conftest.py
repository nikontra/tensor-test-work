import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def browser():
    options_chrome = ChromeOptions()
    options_chrome.add_experimental_option("prefs", {
        "download.default_directory": os.path.abspath(os.path.dirname(__file__)),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    })
    browser = webdriver.Chrome(options=options_chrome)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
