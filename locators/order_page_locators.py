from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPageLocators(BasePage):
    BUTTON_LOCATOR = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO_LIST_FIELD = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    METRO_STATION = (By.CSS_SELECTOR, 'div.Order_Text__2broi')
    BUTTON_NEXT = (By.XPATH, "//button[text() = 'Далее']")
    BUTTON_COOKIE = (By.XPATH, "//button[@id='rcc-confirm-button']")
    TITLE_RENT = (By.XPATH, "//div[text()='Про аренду']")
    DATE_RENT = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    PERIOD_ORDER = (By.CSS_SELECTOR, '.Dropdown-placeholder')
    DAY_ORDER = (By.XPATH, "//div[@class='Dropdown-option'and text()='сутки']")
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'and text()='Заказать']")
    BUTTON_STATUS = (
    By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'and text()='Посмотреть статус']")
    BUTTON_CANCEL = (
    By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'and text()='Отменить заказ']")
    LOGO_SCOOTER = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')
    LOGO_YANDEX = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')
    TITLE_ACCESS = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, "//button[text() = 'Да']")
    SUCCESS_ORDER_TITLE = (By.XPATH, "//div[text() = 'Заказ оформлен']")
    TITLE_NEWS = (By.XPATH, "//div[text() = 'Новости']")