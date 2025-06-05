from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
wait = WebDriverWait(driver, 20)


def test_form_validation():
    # 1. Открыть страницу
    driver.get(" https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Заполнить форму данным
    driver.find_element("xpath", "//input[@name='first-name']").send_keys("Иван")
    driver.find_element("xpath", "//input[@name='last-name']").send_keys("Петров")
    driver.find_element("xpath", "//input[@name='address']").send_keys("Ленина, 55-3")
    driver.find_element("xpath", "//input[@name='e-mail']").send_keys("test@skypro.com")
    driver.find_element("xpath", "//input[@name='phone']").send_keys("+7985899998787")
    # Поле Zip code оставляем пустым
    driver.find_element("xpath", "//input[@name='city']").send_keys("Москва")
    driver.find_element("xpath", "//input[@name='country']").send_keys("Россия")
    driver.find_element("xpath", "//input[@name='job-position']").send_keys("QA")
    driver.find_element("xpath", "//input[@name='company']").send_keys("SkyPro")

    # 3. Нажать кнопку Submit
    button = wait.until(EC.element_to_be_clickable(("xpath", "//button[@type='submit']")))
    button.click()

    # 3. Проверка поля Zip code(красная подсветка)
    zip_code = driver.find_element("xpath", "//div[@id='zip-code']")
    color = zip_code.value_of_css_property("background-color")
    assert color == 'rgba(248, 215, 218, 1)', f"Ожидаемый цвет: rgba(248, 215, 218, 1), Фактический цвет: {color}"

    # 4. Проверка остальных полей(зеленая подсветка)
    valid_fields = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]

    for field in valid_fields:
        element = driver.find_element("css selector", field)
        assert element.value_of_css_property("background-color") == 'rgba(209, 231, 221, 1)', (f"Ожидаемый цвет: rgba("
                                                                                               f"248, 215, 218, 1), "
                                                                                               f"Фактический цвет: "
                                                                                               f"{color}")

    driver.quit()
