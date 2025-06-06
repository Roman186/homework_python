from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 45)


def test_calc_result():
    # Загрузка страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Убираем время в поле
    time_button = driver.find_element("xpath", "//input[@id='delay']")
    time_button.clear()

    # Ввод времени в поле
    time_button.send_keys("45")

    # Нажатие кнопок
    driver.find_element("xpath", "//span[text()='7']").click()
    driver.find_element("xpath", "//span[text()='+']").click()
    driver.find_element("xpath", "//span[text()='8']").click()
    driver.find_element("xpath", "//span[text()='=']").click()

    # Проверка результата
    result = wait.until(EC.text_to_be_present_in_element(("xpath", "//div[@class='screen']"), "15"))
    assert result is True, "Результат не равен 15"

    driver.quit()
