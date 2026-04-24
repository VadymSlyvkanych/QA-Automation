import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    drv = webdriver.Firefox()
    drv.maximize_window()
    yield drv
    drv.quit()


def test_payment_methods_section(driver):
    driver.get("https://itcareerhub.de/ru")
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Способы оплаты"))
    )
    href = link.get_attribute('href')
    anchor_id = href.split('#')[-1]
    payment_section = driver.find_element(By.ID, anchor_id)
    payment_section.screenshot("hw_02/payment_methods_section_.png")


# uv add selenium
# brew install firefox
# uv run pytest hw_02/test_selenium.py -v -s