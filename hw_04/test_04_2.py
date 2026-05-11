import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()


class TestLoadingImages:
    """Проверяем загрузку изображений и атрибуты alt"""

    def test_third_image_alt_is_award(self, driver):
        images = WebDriverWait(driver, 20).until(
            lambda d: d.find_elements(By.CSS_SELECTOR, "#image-container img")
            if len(d.find_elements(By.CSS_SELECTOR, "#image-container img")) >= 4
            else False
        )
        assert images[2].get_attribute("alt") == "award"

# uv run pytest hw_04/test_04_2.py -s --tb=short