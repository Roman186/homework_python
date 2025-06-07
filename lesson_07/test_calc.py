import pytest
from selenium import webdriver
from calc_page import Calc


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"))
    yield driver
    driver.quit()


def test_calc(driver):
    calc = Calc(driver)
    calc.input_time("45")
    calc.click_number()
    result = calc.check_result()

    assert result is True, "Значение не равно 15"
