import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()


class TestIframes:
    def test_iframe(self, driver):
        wait = WebDriverWait(driver, 10)

        iframe = wait.until(
            EC.presence_of_element_located((By.ID, "my-iframe"))
        )

        driver.switch_to.frame(iframe)

        target_text = "semper posuere integer et senectus justo curabitur."

        elements = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f"//*[contains(normalize-space(.), '{target_text}')]")
            )
        )

        # print(elements[-1].text)
        # print(elements[-1].tag_name)
        assert elements[-1].tag_name == "p"


# uv run pytest hw_05/test_05_1.py -s --tb=short
