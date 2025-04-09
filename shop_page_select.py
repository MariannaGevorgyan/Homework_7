from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product:
    def __init__(self, driver):
        self.driver = driver

    def wait_load(self, timeout, element):
        WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located(By.CLASS_NAME, element)))


     def select_item(self, item_id):
        self.driver.find_element(By.ID, item_id).click()


    def cart(self, item_class):
        self.driver.find_element(By.CLASS_NAME, item_class).click()