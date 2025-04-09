from selenium import webdriver
from calc_page_object import Calculator


def test_calculator_form():
    browser = webdriver.Chrome()

    try:
        calculator = Calculator(browser)
        calculator.set_delay(45)
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')
        result_field = calculator.wait_result_field(50)
        assert result_field.text == '15', \
            f"expected result '15', but printed '{result_field.text}'"

        print("test passed successfully: result '15' printed later.")

    finally:
        browser.quit()