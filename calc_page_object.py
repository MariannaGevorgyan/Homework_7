from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__ (self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):

        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button):
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    def wait_result_field(self, timeout):
        WebDriverWait(self.driver, timeout=timeout).until(
            EC.invisibility_of_element_located((By.ID, 'spinner'))
        )

        result_field = self.driver.find_element(By. CLASS_NAME, 'screen')
        return result_field