import pytest
from selenium import webdriver
import data


@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    firefox_driver = webdriver.Firefox(options=options)
    firefox_driver.maximize_window()
    firefox_driver.get(data.Urls.URL)
    yield firefox_driver
    firefox_driver.quit()