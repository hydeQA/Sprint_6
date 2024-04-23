from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    @allure.step ("Открыть в браузере Firefox страницу 'Яндекс Самокат'")
    def open(self):
        self.driver.get(data.Urls.URL)
    @allure.step ("Кликнуть на кнопку вопроса {question_index}")
    def click_question(self, question_index):
        question_locator = (By.XPATH, f"//div[@id='accordion__heading-{question_index}']")
        question_element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(question_locator))
        question_element.click()

    def get_answer_text(self, question_index):
        answer_locator = (By.ID, f'accordion__panel-{question_index}')
        answer_element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(answer_locator))
        return answer_element.text
