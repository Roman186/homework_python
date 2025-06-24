import allure
import pytest
from selenium import webdriver
from calc_page import Calc


@pytest.fixture()
def driver():
    """
    Инициализирует webdriver. Запускает браузер Chrome.
    Переходит на сайт.
    После выполнения теста закрывает браузер.
    """

    with allure.step("Запустить браузер"):
        driver = webdriver.Chrome()
    driver.maximize_window()
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"))
    yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Получение итогового результата")
@allure.description("Проверка: полученный результат == ожидаемому")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver):
    calc = Calc(driver)
    with allure.step("Ввод времени в поле ввода"):
        calc.input_time("45")
    with allure.step("Клик по кнопкам на калькуляторе"):
        calc.click_number()
    with allure.step("Получить конечный результат операции"):
        result = calc.check_result()
    with allure.step("Проверить, что полученное значение == ожидаемому"):
        assert result is True, "Значение не равно 15"
