from selenium.webdriver.common.by import By

class Authorization:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://www.saucedemo.com/")

    def input_auth(self, username, password):
            username_field = self.driver.find_element(By.ID, "user-name")
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "login-button")

            username_field.send_keys(username)
            password_field.send_keys(password)
            login_button.click()