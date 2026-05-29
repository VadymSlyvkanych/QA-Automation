from selenium.webdriver.common.by import By
from hw_06.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self._send_keys(self.USERNAME_INPUT, username)
        self._send_keys(self.PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)
