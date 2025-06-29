from selenium.webdriver.common.by import By


class BasePageLocators:
    """Локаторы общие для всех страниц"""
    pass


class SabyMainPageLocators:
    """Локаторы для главной страницы Saby"""
    MENU_CONTACTS = (By.CSS_SELECTOR, ".sbisru-Header ul li:nth-child(2)")
    CONTACTS_PAGE = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu__items .sbisru-link")


class SabyContactsLocators:
    """Локаторы для страницы контактов Saby"""
    TENSOR_PAGE = (By.CSS_SELECTOR, "#contacts_clients .sbisru-Contacts__border-left a")


class TensorMainLocators:
    """Локаторы для главной страницы Tensor"""
    STRENGTH_IN_PEOPLE = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p:nth-child(1)")
    ABOUT_PAGE = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p:nth-child(4) a")


class TensorAboutLocators:
    """Локаторы для страницы 'О компании Тензор'"""
    IMAGES = (By.CSS_SELECTOR, ".tensor_ru-About__block3 img")
