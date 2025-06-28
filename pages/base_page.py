from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_contacts_page(self):
        self.browser.find_element(By.CSS_SELECTOR, ".sbisru-Header ul li:nth-child(2)").click()
        self.browser.find_element(By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu__items .sbisru-link").click()

    def go_to_tensor_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#contacts_clients .sbisru-Contacts__border-left a").click()
        tensor_link = self.browser.window_handles[1]
        self.browser.switch_to.window(tensor_link)