import data
import allure
from pages.order_page import OrderPage

class TestOrderButton:

    @allure.title('Проверка успешного заказа самоката по кнопке "Заказать" в шапке сайта')
    def test_order_button_in_bot_page_success(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_cookie_button()

        order_page.click_order_button_2()
        order_page.set_name(data.OrderDetails.NAME_2)
        order_page.set_surname(data.OrderDetails.SURNAME_2)
        order_page.set_address(data.OrderDetails.ADDRESS_2)
        order_page.set_phone_number(data.OrderDetails.PHONE_NUMBER_2)
        order_page.set_metro_station()
        order_page.click_next_button()
        order_page.set_date_rent(data.OrderDetails.RENT_DATE_2)
        order_page.set_rental_period()
        order_page.click_order_button_finally()
        order_page.access_order()

        assert order_page.is_element_present(OrderPage.SUCCESS_ORDER_TITLE), "Заголовок 'Заказ оформлен' не найден"

    @allure.title("Проверка перехода на главную страницу 'Самоката' тапом по лого 'Самокат' в шапке, после успешного оформления заказа")
    def test_button_in_top_page_redirect_to_main_page_success(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_order_button_1()
        order_page.set_name(data.OrderDetails.NAME)
        order_page.set_surname(data.OrderDetails.SURNAME)
        order_page.set_address(data.OrderDetails.ADDRESS)
        order_page.set_phone_number(data.OrderDetails.PHONE_NUMBER)
        order_page.set_metro_station()
        order_page.click_next_button()
        order_page.set_date_rent(data.OrderDetails.RENT_DATE)
        order_page.set_rental_period()
        order_page.click_order_button_finally()
        order_page.access_order()

        order_page.click_button_status()
        order_page.click_scooter_logo()

        assert driver.current_url == data.Urls.URL

    @allure.title("Проверка перехода на главную страницу 'Дзена' тапом по лого 'Яндекс' в шапке, после успешного оформления заказа через нижнюю кнопку 'Заказать'")
    def test_button_in_top_page_redirect_to_dzen_page_success(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        
        order_page.click_order_button_1()
        order_page.set_name(data.OrderDetails.NAME)
        order_page.set_surname(data.OrderDetails.SURNAME)
        order_page.set_address(data.OrderDetails.ADDRESS)
        order_page.set_phone_number(data.OrderDetails.PHONE_NUMBER)
        order_page.set_metro_station()
        order_page.click_next_button()
        order_page.set_date_rent(data.OrderDetails.RENT_DATE)
        order_page.set_rental_period()
        order_page.click_order_button_finally()
        order_page.access_order()

        order_page.click_button_status()
        order_page.click_yandex_logo()
        order_page.switch_to_new_tab()

        assert driver.current_url == data.Urls.URL_DZEN