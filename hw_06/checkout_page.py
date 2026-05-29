from selenium.webdriver.common.by import By
from hw_06.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def fill_form(self, first_name, last_name, postal_code):
        self._set_react_input(self.FIRST_NAME_INPUT, first_name)
        self._set_react_input(self.LAST_NAME_INPUT, last_name)
        self._set_react_input(self.POSTAL_CODE_INPUT, postal_code)

        self.driver.execute_script("""
            document.querySelector('form').addEventListener(
                'submit', function(e) { e.preventDefault(); }, true
            );
        """)
        self._click(self.CONTINUE_BUTTON)
