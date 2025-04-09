from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Form:

    def __init__(self, driver):
        self.driver = driver

    def wait_load_id(self, timeout, element):
        WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located(By.ID, element)))

    def fill_form(self, field, value):
        self.driver.find_element(By.ID, field).send_keys(value)

    def click_form(self, button):
        self.driver.find_element(By.ID, button).click()

    def overwiew(self, item):
        total_element = self.driver.find_element(By.CLASS_NAME, item)
        total_text = total_element.text
        total_value = float(total_text.split("$")[1])
        return total_value