from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_add_to_basket_button_present(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    
    # Пауза для визуальной проверки языка
    time.sleep(15)
    
    # Проверяем наличие кнопки добавления в корзину
    add_to_basket_button = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    assert add_to_basket_button.is_displayed(), "Button is not displayed"
