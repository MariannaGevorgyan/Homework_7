from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator:

    def __init__(self, driver):
        """Конструктор класса калькулятора."""
        self.driver = driver
        with allure.step("Открыть страницу калькулятора"):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        """Настроить задержку калькулятора."""
        with allure.step(f"Установить задержку ввода в калькулятор ({delay}) сек."):
            delay_input = self.driver.find_element(By.ID, 'delay')
            delay_input.clear()
            delay_input.send_keys(delay)

    def click_button(self, button):
        """Метод кликает на заданную кнопку калькулятора."""
        with allure.step(f"Кликнуть на кнопку калькулятора ('{button}')"):
            self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    def wait_result_field(self, timeout):
        """Ждать исчезновения индикатора загрузки и возвращать элемент результата."""
        with allure.step(f"Дождаться завершения расчёта (до {timeout} сек.)"):
            WebDriverWait(self.driver, timeout=timeout).until(
                EC.invisibility_of_element_located((By.XPATH, 'spinner'))
            )
            result_field = self.driver.find_element(By.CLASS_NAME, 'screen')
            return result_field