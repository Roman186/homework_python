from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Items:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.items_locator = ("xpath", "//div[@class='inventory_item']")

    def add_item(self) -> None:
        """
        Метод добавляет выбранные товары в корзину
        :return: None
        """

        self.wait.until(
            EC.visibility_of_element_located(self.items_locator))
        (self.driver.find_element
         ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click())
        (self.driver.find_element
         ("xpath", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
         .click())
        (self.driver.find_element
         ("xpath", "//button[@id='add-to-cart-sauce-labs-onesie']").click())

    def get_in_cart(self) -> None:
        """
        Переход в корзину товаров
        :return: None
        """

        cart_button = (self.driver.find_element
                       ("xpath", "//a[@class='shopping_cart_link']"))
        cart_button.click()
