from selenium.webdriver.common.by import By
import allure

class Checkout:
    def __init__(self, driver):
        """Инициализация класса Checkout"""
        self.driver = driver

    def button(self, button_id):
        """Метод для нажатия кнопки по ID"""
        with allure.step(f"Нажатие кнопки с идентификатором '{button_id}'"):
            self.driver.find_element(By.ID, button_id).click()