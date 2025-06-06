from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 20)


def test_price_total():
    # Загрузка страницы
    driver.get("https://www.saucedemo.com")

    # Авторизация
    driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@id='login-button']").click()

    # Ожидаем загрузки товаров на странице
    ITEMS_LOCATOR = ("xpath", "//div[@class='inventory_item']")
    wait.until(EC.visibility_of_element_located(ITEMS_LOCATOR))

    # Добавление товаров в корзину
    driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-onesie']").click()

    # Переход в корзину
    driver.find_element("xpath", "//a[@data-test='shopping-cart-link']").click()

    # Клик по кнопке "Checkout"
    driver.find_element("xpath", "//button[@id='checkout']").click()

    # Заполнение формы данными
    driver.find_element("xpath", "//input[@id='first-name']").send_keys("Иван")
    driver.find_element("xpath", "//input[@id='last-name']").send_keys("Петров")
    driver.find_element("xpath", "//input[@id='postal-code']").send_keys("628600")

    # Клик по кнопке "Continue"
    driver.find_element("xpath", "//input[@id='continue']").click()

    # Получение итоговой суммы
    wait.until(EC.visibility_of_element_located(("xpath", "//div[@class='summary_total_label']")))
    total_cost = driver.find_element("xpath", "//div[@class='summary_total_label']").text

    # Проверка итоговой суммы
    total = total_cost.replace('Total:', '').strip()
    assert total == "$58.29", f"Ожидаемая сумма: $58.29, Фактическая: {total}"

    driver.quit()
