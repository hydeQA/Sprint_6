from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    def open_page(self, url):
        self.driver.get(url)


    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False


    def switch_to_new_tab(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))