import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    drv = webdriver.Firefox()
    drv.maximize_window()
    yield drv
    drv.quit()


def test_payment_methods_section(driver):
    driver.get("https://itcareerhub.de/ru")
    time.sleep(2)
    link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    link.click()
    time.sleep(2)
    driver.save_screenshot("hw_02/payment_methods_section.png")


# uv add selenium
# brew install firefox
# uv run pytest hw_02/selenium_test.py -v -s