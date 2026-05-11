import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()


class TestTextInput:
    """Проверяем изменение текста кнопки после ввода значения в поле"""

    def test_button_text_changes_after_input(self, driver):
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "newButtonName"))
        )
        input_field.clear()
        input_field.send_keys("ITCH")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "updatingButton"))
        ).click()

        updated_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[text()="ITCH"]'))
        )
        assert updated_btn.text == "ITCH"

# uv run pytest hw_04/test_04_1.py -s --tb=short