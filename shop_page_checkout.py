from selenium.webdriver.common.by import By


class Checkout:
    def __init_(self, driver):
        self.driver = driver

    def button(self, button_id):
        self.driver.find_element(By.ID, button_id).click()
