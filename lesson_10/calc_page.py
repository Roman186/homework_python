from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)
        self.time_locator = ("xpath", "//input[@id='delay']")

    def input_time(self, query: str) -> None:
        """
            Вводит время в поле ввода.

            :param query: Время
            :type query: Str
            :return: None
        """

        time_button = self.driver.find_element(*self.time_locator)
        time_button.clear()
        time_button.send_keys(query)

    def click_number(self) -> None:
        """
            Клик кнопок на калькуляторе.
            :return: None
        """

        self.driver.find_element("xpath", "//span[text()='7']").click()
        self.driver.find_element("xpath", "//span[text()='+']").click()
        self.driver.find_element("xpath", "//span[text()='8']").click()
        self.driver.find_element("xpath", "//span[text()='=']").click()

    def check_result(self) -> bool:
        """
            Проверяет конечный результат операции,
            который отобразится в окне.
            :return: Bool
        """

        result = self.wait.until(
            EC.text_to_be_present_in_element(
                ("xpath", "//div[@class='screen']"), "15"))
        return result
