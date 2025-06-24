from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Order:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self) -> None:
        """
        Метод заполняет форму заказа данными
        и нажимает кнопку continue
        :return: None
        """
        (self.driver.find_element
         ("xpath", "//input[@id='first-name']").send_keys("Иван"))
        (self.driver.find_element
         ("xpath", "//input[@id='last-name']").send_keys("Петров"))
        (self.driver.find_element
         ("xpath", "//input[@id='postal-code']").send_keys("628600"))
        (self.driver.find_element
         ("xpath", "//input[@id='continue']").click())

    def check_total_price(self) -> str:
        """
        Метод получает итоговую стоимость заказа
        и возвращает результат
        :return: str
        """
        self.wait.until(
            EC.visibility_of_element_located(
                ("xpath", "//div[@class='summary_total_label']")))

        total_cost = (self.driver.find_element
                      ("xpath", "//div[@class='summary_total_label']").text)
        total = total_cost.replace('Total:', '').strip()

        return total
