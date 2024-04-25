from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = lambda question_index: (By.XPATH, f"//div[@id='accordion__heading-{question_index}']")
    ANSWER_LOCATOR = lambda question_index: (By.ID, f'accordion__panel-{question_index}')
