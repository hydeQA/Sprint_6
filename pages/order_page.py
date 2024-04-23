from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage(BasePage):

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
    BUTTON_STATUS = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'and text()='Посмотреть статус']")
    BUTTON_CANCEL = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'and text()='Отменить заказ']")

    LOGO_SCOOTER = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')
    LOGO_YANDEX = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')

    TITLE_ACCESS = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, "//button[text() = 'Да']")

    SUCCESS_ORDER_TITLE = (By.XPATH, "//div[text() = 'Заказ оформлен']")
    TITLE_NEWS = (By.XPATH, "//div[text() = 'Новости']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть в браузере Firefox страницу 'Яндекс Самокат'")
    def open(self):
        self.driver.get(data.Urls.URL)
    @allure.step("Кликнуть по кнопке 'Заказать' в шапке страницы")
    def click_order_button_1(self):
        order_button = self.wait_and_find_element(self.BUTTON_LOCATOR)
        order_button.click()
    @allure.step('Кликнуть по кнопке "Да все привыкли" и принять cookie сайта')
    def click_cookie_button(self):
        cookie_button = self.wait_and_find_element(self.BUTTON_COOKIE)
        cookie_button.click()
    @allure.step('Кликнуть по кнопке "Заказать" внизу страницы')
    def click_order_button_2(self):
        order_button_2 = self.wait_and_find_element(self.BUTTON_ORDER)
        order_button_2.click()
    @allure.step('Ввести в поле "Имя": {name}')
    def set_name(self, name):
        set_name_field = self.wait_and_find_element(self.NAME_FIELD)
        set_name_field.send_keys(name)
    @allure.step('Ввести в поле "Фамилия": {surname}')
    def set_surname(self, surname):
        set_surname_field = self.wait_and_find_element(self.SURNAME_FIELD)
        set_surname_field.send_keys(surname)
    @allure.step('Ввести в поле "Адрес": {address}')
    def set_address(self, address):
        set_address_field = self.wait_and_find_element(self.ADDRESS_FIELD)
        set_address_field.send_keys(address)
    @allure.step('Ввести в поле "Телефон": {phone_number}')
    def set_phone_number(self, phone_number):
        set_phone_number_field = self.wait_and_find_element(self.PHONE_NUMBER_FIELD)
        set_phone_number_field.send_keys(phone_number)
    @allure.step('Выбрать станцию метро из выпадающего списка')
    def set_metro_station(self):
        station_list = self.wait_and_find_element(self.METRO_LIST_FIELD)
        station_list.click()
        station = self.wait_and_find_element(self.METRO_STATION)
        station.click()
    @allure.step('Перейти на следующую страницу кликом по кнопке "Далее"')
    def click_next_button(self):
        button = self.wait_and_find_element(self.BUTTON_NEXT)
        button.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.TITLE_RENT))
    @allure.step('Написать дату аренды самоката {date_rent} и нажать Enter')
    def set_date_rent(self, date_rent):
        date_rent_field = self.wait_and_find_element(self.DATE_RENT)
        date_rent_field.send_keys(date_rent)
        date_rent_field.send_keys(Keys.ENTER)
    @allure.step('Выбрать период аренды из выпадающего списка "сутки"')
    def set_rental_period(self):
        rent_period_field = self.wait_and_find_element(self.PERIOD_ORDER)
        rent_period_field.click()
        set_period = self.wait_and_find_element(self.DAY_ORDER)
        set_period.click()
    @allure.step('Кликнуть на кнопку "Заказать" для завершения заказа')
    def click_order_button_finally(self):
        order_button = self.wait_and_find_element(self.BUTTON_ORDER)
        order_button.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.TITLE_RENT))
    @allure.step('Подтвердить заказ кликом по кнопке "Да" на всплывающем окне "Хотите оформить заказ?"')
    def access_order(self):
        button_yes = self.wait_and_find_element(self.BUTTON_YES)
        button_yes.click()

    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    @allure.step('Кликнуть на кнопку "Посмотреть статус" на всплывающем окне "Заказ оформлен"')
    def click_button_status(self):
        status_button = self.wait_and_find_element(self.BUTTON_STATUS)
        status_button.click()
    @allure.step ("Кликнуть на логотип 'Самокат' для завершения заказа")
    def click_scooter_logo(self):
        scooter_button = self.wait_and_find_element(self.LOGO_SCOOTER)
        scooter_button.click()
    @allure.step ("Кликнуть на логотип 'Яндекс' в шапке страницы")
    def click_yandex_logo(self):
        yandex_button = self.wait_and_find_element(self.LOGO_YANDEX)
        yandex_button.click()

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.TITLE_NEWS))