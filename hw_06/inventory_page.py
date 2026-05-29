from selenium.webdriver.common.by import By
from hw_06.base_page import BasePage


class InventoryPage(BasePage):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def _get_add_to_cart_button(self, item_name):
        item_slug = item_name.lower().replace(" ", "-")
        return By.ID, f"add-to-cart-{item_slug}"

    def add_item_to_cart(self, item_name):
        button_locator = self._get_add_to_cart_button(item_name)
        self._click(button_locator)

    def go_to_cart(self):
        self._click(self.CART_LINK)
