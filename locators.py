from selenium.webdriver.common.by import By


class BasePageLocators:
    """Локаторы общие для всех страниц"""
    pass


class SabyMainPageLocators:
    """Локаторы для главной страницы Saby"""
    MENU_CONTACTS = (By.CSS_SELECTOR, ".sbisru-Header ul li:nth-child(2)")
    CONTACTS_PAGE = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu__items .sbisru-link")
    DOWNLOAD = (By.CSS_SELECTOR, 'a[href="/download"]')


class SabyContactsLocators:
    """Локаторы для страницы контактов Saby"""
    TENSOR_PAGE = (By.CSS_SELECTOR, "#contacts_clients .sbisru-Contacts__border-left a")
    REGION = (By.CSS_SELECTOR, ".sbisru-Contacts__underline .sbis_ru-Region-Chooser__text")
    NEW_REGION = (By.CSS_SELECTOR, 'ul.sbis_ru-Region-Panel__list-l li [title="Камчатский край"]')
    LIST_PARTNERS = (By.CSS_SELECTOR, ".sbisru-Contacts-List__name")


class TensorMainLocators:
    """Локаторы для главной страницы Tensor"""
    STRENGTH_IN_PEOPLE = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p:nth-child(1)")
    ABOUT_PAGE = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p:nth-child(4) a")


class TensorAboutLocators:
    """Локаторы для страницы 'О компании Тензор'"""
    IMAGES = (By.CSS_SELECTOR, ".tensor_ru-About__block3 img")


class TensorDownloadLocators:
    """Локаторы для страницы загрузок"""
    DOWNLOAD_PLUGIN = (By.XPATH, '//div[@class="ws-SwitchableArea sbis_ru-VerticalTabs__area ws-enabled ws-component'
                                 ' ws-has-focus"]//div[@class="ws-SwitchableArea__item ws-component'
                                 ' ws-enabled ws-has-focus"]/div[2]//a')
