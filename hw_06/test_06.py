import pytest
from selenium import webdriver

from hw_06.login_page import LoginPage
from hw_06.inventory_page import InventoryPage
from hw_06.cart_page import CartPage
from hw_06.checkout_page import CheckoutPage
from hw_06.checkout_overview_page import CheckoutOverviewPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


class TestPurchaseFlow:
    def test_complete_purchase(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("John", "Doe", "12345")

        checkout_overview_page = CheckoutOverviewPage(driver)
        total = checkout_overview_page.get_total()

        assert total == "Total: $58.29"
