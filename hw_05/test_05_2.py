import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Блокируем Funding Choices, чтобы не подгружалась проверка куков с https://fundingchoicesmessages.google.com
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setBlockedURLs", {
        "urls": [
            "*fundingchoices*"
        ]
    })
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()


class TestDragAndDrop:
    def test_drag_and_drop(self, driver):
        wait = WebDriverWait(driver, 10)

        # driver.execute_script("""
        #     const consent = document.querySelector('.fc-consent-root');
        #     if (consent) consent.remove();
        # """)

        wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.demo-frame[src*='photo-manager.html']")
            )
        )

        first_photo = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//ul[@id='gallery']/li)[1]")
            )
        )

        trash = wait.until(
            EC.presence_of_element_located((By.ID, "trash"))
        )

        ActionChains(driver).drag_and_drop(first_photo, trash).perform()

        trash_photos = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@id='trash']//li")
            )
        )
        assert len(trash_photos) == 1

        gallery_photos = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@id='gallery']/li")
            )
        )
        assert len(gallery_photos) == 3


# uv run pytest hw_05/test_05_2.py -s --tb=short
