from selenium.webdriver.common.by import By
from hw_06.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self._click(self.CHECKOUT_BUTTON)
