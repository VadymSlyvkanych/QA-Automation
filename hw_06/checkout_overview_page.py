from selenium.webdriver.common.by import By
from hw_06.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def get_total(self):
        return self._get_text(self.TOTAL_LABEL)
