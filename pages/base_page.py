
class BasePage:
    """Класс методов общих для всех страниц"""
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Метод открывает страницу"""
        self.browser.get(self.url)

    def get_link(self, locator):
        """Метод возвращает ссылку элемента"""
        link_download = self.browser.find_element(*locator)
        return link_download.get_attribute('href')

    def should_be_link(self, url):
        """Метод проверяет корректность URL"""
        assert self.browser.current_url == url, "Не правильный адрес страницы"
