import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()


def get_visible(driver, by, selector, timeout=10):
    """Ждёт элемент, проверяет видимость и возвращает его"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, selector)),
        message=f"Элемент не найден или не виден: {by}='{selector}'"
    )


def get_clickable(driver, by, selector, timeout=10):
    """Ждёт элемент, проверяет что кликабелен и возвращает его"""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector)),
        message=f"Элемент не кликабелен: {by}='{selector}'"
    )


class TestHomePage:
    """Проверяем наличие всех ключевых элементов на главной странице"""
    def test_logo_is_displayed(self, driver):
        assert get_visible(driver, By.CSS_SELECTOR, 'img[alt="IT Career Hub"]')


    @pytest.mark.parametrize("link_text", [
        "Программы",
        "Способы оплаты",
        "О нас",
        "Отзывы",
        "Блог",
        "ru",
        "de"
    ])
    def test_nav_links_visible(self, driver, link_text):
        assert get_visible(driver, By.LINK_TEXT, link_text)


class TestContactsFlow:
    """Тесты сценария: Контакты → Обратный звонок → всплывающее окно"""
    def test_callback_popup_text(self, driver):
        get_clickable(driver, By.LINK_TEXT, "О нас").click()
        get_clickable(driver, By.LINK_TEXT, "Контакты").click()
        WebDriverWait(driver, 15).until(EC.url_contains("contact-us"))
        # в задании: 4. Кликнуть по кнопке “Обратный звонокˮ
        btn = get_clickable(driver, By.LINK_TEXT, "ОБРАТНЫЙ ЗВОНОК")
        driver.execute_script("arguments[0].click();", btn)
        expected = "Запишитесь на бесплатную карьерную консультацию"
        # . — весь текст включая дочерние теги
        assert get_visible(driver, By.XPATH, f'//*[contains(., "{expected}")]')

# uv run pytest hw_03/test_03.py -s --tb=short
