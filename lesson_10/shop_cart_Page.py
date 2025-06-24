from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def count_items(self) -> int:
        """
        Метод считает количество товаров лежащих в корзине
        и возвращает результат в виде числа
        :return: int
        """

        self.wait.until(
            EC.visibility_of_element_located(
                ("xpath", "//div[@class='cart_item']")))
        count = self.driver.find_elements("xpath", "//div[@class='cart_item']")
        return len(count)

    def added_items(self) -> list:
        """
        Метод ищет названия товаров лежащих в корзине и
        возвращает список этих названий
        :return: list
        """
        cart_items = (self.driver.find_elements
                      ("xpath", "//div[@class='cart_item']"))

        actual_items = []
        for item in cart_items:
            name = item.find_element("xpath", ".//div\
            [@class='inventory_item_name']").text.strip()
            actual_items.append(name)

        return actual_items

    def button_checkout(self) -> None:
        """
        Ждет появление кнопки checkout и нажимает на нее
        :return: None
        """
        self.wait.until(
            EC.visibility_of_element_located(
                ("xpath", "//button[@id='checkout']")))
        (self.driver.find_element
         ("xpath", "//button[@id='checkout']").click())
