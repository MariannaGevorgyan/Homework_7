from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class Form:

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    def wait_load_id(self, timeout, element):
        """Ожидает загрузки элемента по его id"""
        with allure.step(f"Ожидание загрузки элемента с id '{element}' в течение {timeout} секунд"):
            WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located((By.ID, element)))

    def fill_form(self, field, value):
        """Заполняет поле формы указанным значением"""
        with allure.step(f"Введение значения '{value}' в поле с id '{field}'"):
            self.driver.find_element(By.ID, field).send_keys(value)

    def click_form(self, button):
        """Кликает на указанную кнопку"""
        with allure.step(f"Клик на кнопку с id '{button}'"):
            self.driver.find_element(By.ID, button).click()

    def overview(self, item):
        """Получает итоговое значение цены"""
        with allure.step(f"Получение итогового значения элемента с class '{item}'"):
            total_element = self.driver.find_element(By.CLASS_NAME, item)
            total_text = total_element.text
            total_value = float(total_text.split("$")[1])
            return total_value