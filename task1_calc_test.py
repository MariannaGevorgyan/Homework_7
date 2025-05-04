from selenium import webdriver
from calc_page_object import Calculator
from selenium.webdriver.common.by import By
import time


def test_calculator_form():
    browser = webdriver.Chrome()
    browser.maximize_window()

    try:

        calculator = Calculator(browser)
        calculator.set_delay(45)
        calculator.click_button('7')
        time.sleep(2)
        calculator.click_button('+')
        time.sleep(2)
        calculator.click_button('8')
        button = browser.find_element(By.XPATH, '//span[text()="="]')
        browser.execute_script("arguments[0].scrollIntoView();", button)
        calculator.click_button('=')
        time.sleep(2)
        result_field = calculator.wait_result_field(50)
        assert result_field.text == '15', \
            f"expected result '15', but printed '{result_field.text}'"

        print("test passed successfully: result '15' printed later.")

    finally:
        browser.quit()