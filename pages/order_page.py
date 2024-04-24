from pages.base_page import BasePage
import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import allure
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Открыть в браузере Firefox страницу 'Яндекс Самокат'")
    def open(self):
        self.driver.get(data.Urls.URL)


    @allure.step("Кликнуть по кнопке 'Заказать' в шапке страницы")
    def click_order_button_1(self):
        order_button = self.wait_and_find_element(OrderPageLocators.BUTTON_LOCATOR)
        order_button.click()


    @allure.step('Кликнуть по кнопке "Да все привыкли" и принять cookie сайта')
    def click_cookie_button(self):
        cookie_button = self.wait_and_find_element(OrderPageLocators.BUTTON_COOKIE)
        cookie_button.click()


    @allure.step('Кликнуть по кнопке "Заказать" внизу страницы')
    def click_order_button_2(self):
        order_button_2 = self.wait_and_find_element(OrderPageLocators.BUTTON_ORDER)
        order_button_2.click()


    @allure.step('Ввести в поле "Имя": {name}')
    def set_name(self, name):
        set_name_field = self.wait_and_find_element(OrderPageLocators.NAME_FIELD)
        set_name_field.send_keys(name)


    @allure.step('Ввести в поле "Фамилия": {surname}')
    def set_surname(self, surname):
        set_surname_field = self.wait_and_find_element(OrderPageLocators.SURNAME_FIELD)
        set_surname_field.send_keys(surname)


    @allure.step('Ввести в поле "Адрес": {address}')
    def set_address(self, address):
        set_address_field = self.wait_and_find_element(OrderPageLocators.ADDRESS_FIELD)
        set_address_field.send_keys(address)


    @allure.step('Ввести в поле "Телефон": {phone_number}')
    def set_phone_number(self, phone_number):
        set_phone_number_field = self.wait_and_find_element(OrderPageLocators.PHONE_NUMBER_FIELD)
        set_phone_number_field.send_keys(phone_number)


    @allure.step('Выбрать станцию метро из выпадающего списка')
    def set_metro_station(self):
        station_list = self.wait_and_find_element(OrderPageLocators.METRO_LIST_FIELD)
        station_list.click()
        station = self.wait_and_find_element(OrderPageLocators.METRO_STATION)
        station.click()


    @allure.step('Перейти на следующую страницу кликом по кнопке "Далее"')
    def click_next_button(self):
        button = self.wait_and_find_element(OrderPageLocators.BUTTON_NEXT)
        button.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.TITLE_RENT))


    @allure.step('Написать дату аренды самоката {date_rent} и нажать Enter')
    def set_date_rent(self, date_rent):
        date_rent_field = self.wait_and_find_element(OrderPageLocators.DATE_RENT)
        date_rent_field.send_keys(date_rent)
        date_rent_field.send_keys(Keys.ENTER)


    @allure.step('Выбрать период аренды из выпадающего списка "сутки"')
    def set_rental_period(self):
        rent_period_field = self.wait_and_find_element(OrderPageLocators.PERIOD_ORDER)
        rent_period_field.click()
        set_period = self.wait_and_find_element(OrderPageLocators.DAY_ORDER)
        set_period.click()


    @allure.step('Кликнуть на кнопку "Заказать" для завершения заказа')
    def click_order_button_finally(self):
        order_button = self.wait_and_find_element(OrderPageLocators.BUTTON_ORDER)
        order_button.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.TITLE_RENT))


    @allure.step('Подтвердить заказ кликом по кнопке "Да" на всплывающем окне "Хотите оформить заказ?"')
    def access_order(self):
        button_yes = self.wait_and_find_element(OrderPageLocators.BUTTON_YES)
        button_yes.click()


    @allure.step('Кликнуть на кнопку "Посмотреть статус" на всплывающем окне "Заказ оформлен"')
    def click_button_status(self):
        status_button = self.wait_and_find_element(OrderPageLocators.BUTTON_STATUS)
        status_button.click()


    @allure.step ("Кликнуть на логотип 'Самокат' для завершения заказа")
    def click_scooter_logo(self):
        scooter_button = self.wait_and_find_element(OrderPageLocators.LOGO_SCOOTER)
        scooter_button.click()


    @allure.step ("Кликнуть на логотип 'Яндекс' в шапке страницы")
    def click_yandex_logo(self):
        yandex_button = self.wait_and_find_element(OrderPageLocators.LOGO_YANDEX)
        yandex_button.click()
