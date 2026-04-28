from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

CONFIG = {
    'base_url': 'https://www.saucedemo.com/',
    'window_size': (1920, 1080),
}


def get_driver():
    # Настройка опций Chrome
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "plugins.always_open_pdf_externally": True,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.media_stream": 2,
        "translate": {"enabled": False},
    }
    options.add_experimental_option("prefs", prefs)

    # Создание драйвера
    driver = webdriver.Chrome(
        options=options,
        service=ChromeService(ChromeDriverManager().install())
    )

    # Настройка окна
    driver.set_window_size(*CONFIG['window_size'])

    print("Драйвер инициализирован")
    return driver


# Класс с тестами
class TestCreatePlace:
    # Тест создания отчёта Allure
    def test_create_allure_report(self):
        driver = get_driver()
        try:
            # Открытие браузера по указаному URL
            driver.get(CONFIG['base_url'])
        except TimeoutException:
            print(f"\nТЕСТ ПРОВАЛЕН (Timeout): {TimeoutException}")
        finally:
            if driver:
                time.sleep(2)
                driver.quit()
                print("\nДрайвер закрыт")
