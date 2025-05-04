from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class Product:
    def __init__(self, driver):
        """Инициализация продукта"""
        self.driver = driver

    def wait_load(self, timeout, element):
        """Ожидание загрузки страницы"""
        with allure.step(f"Ожидание загрузки элемента с классом '{element}' в течение {timeout} секунд"):
            WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, element)))

    def select_item(self, item_id):
        """Выбираем товар по его id"""
        with allure.step(f"Выбор товара с id '{item_id}'"):
            self.driver.find_element(By.ID, item_id).click()

    def cart(self, item_class):
        """Переход в корзину"""
        with allure.step(f"Переход в корзину по классу '{item_class}'"):
            self.driver.find_element(By.CLASS_NAME, item_class).click()