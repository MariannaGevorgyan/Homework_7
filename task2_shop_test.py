from selenium import webdriver
from shop_page_auth import Authorization
from shop_page_select import Product
from shop_page_checkout import Checkout
from shop_page_form import Form


def test_shop():
    browser = webdriver.Chrome()
    browser.maximize_window()
    auth = Authorization(browser)
    auth.input_auth("standard_user", "secret_sauce")

    product = Product(browser)
    product.wait_load(20, "inventory_item")

    product.select_item('add-to-cart-sauce-labs-backpack')
    product.select_item('add-to-cart-sauce-labs-bolt-t-shirt')
    product.select_item('add-to-cart-sauce-labs-onesie')

    product.cart("shopping_cart_link")
    product.wait_load(20, "cart_item")

    checkout = Checkout(browser)
    checkout.button("checkout")

    form = Form(browser)
    form.wait_load_id(20, "first-name")
    form.fill_form("first-name", "Marianna")
    form.fill_form("last-name", "Gevorgyan")
    form.fill_form("postal-code", "171401")

    form.click_form("continue")


    product.wait_load(30, "summary_info")
    total_value = form.overview("summary_total_label")

    expected_total = 58.29
    assert total_value == expected_total, \
        (f"total amount is ${total_value:.2f}, "
         f"expected ${expected_total:.2f}")

    print(f"test passed: total amount is ${total_value:.2f}")

    browser.quit()








