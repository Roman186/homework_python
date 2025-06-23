import allure
import pytest
from selenium import webdriver
from authPage import Authorization
from main_shopPage import Items
from shop_cart_Page import Cart
from shop_orderPage import Order


@pytest.fixture()
def driver():
    """
    Инициализирует webdriver. Запускает браузер Firefox.
    После выполнения теста закрывает браузер.
    """

    with allure.step("Запустить браузер"):
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture()
def auth_driver(driver):
    """
    Переходит на тестируемый сайт.
    Авторизация.
    """

    driver.get("https://www.saucedemo.com")
    auth_page = Authorization(driver)
    with allure.step("Авторизация"):
        auth_page.auth()
    return driver


@allure.title("Тест корзины интернет-магазина")
@allure.description("Проверка количества и названий товаров в корзине")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_cart_shop(auth_driver):
    main_page = Items(auth_driver)
    with allure.step("Добавить товары в корзину"):
        main_page.add_item()
    with allure.step("Перейти в корзину"):
        main_page.get_in_cart()
    cart_page = Cart(auth_driver)
    with allure.step("Посчитать количество товаров"):
        count_result = cart_page.count_items()
    with allure.step(f"Число товаров в корзине: {count_result} == 3"):
        assert count_result == 3, \
            f"Число товаров должно быть 3, в итоге: {count_result}"
    with allure.step("Получить названия товаров в корзине"):
        items_result = cart_page.added_items()
    expected_items = ["Sauce Labs Backpack",
                      "Sauce Labs Bolt T-Shirt",
                      "Sauce Labs Onesie"]
    with allure.step("Названия товаров в корзине == названия добавленных товаров"):
        assert items_result == expected_items, \
            "Названия добавленных товаров \
        не совпадает с названиями товаров в корзине"
    with allure.step("Нажать кнопку checkout"):
        cart_page.button_checkout()


@allure.title("Тестирование формы заказа")
@allure.description("Проверка итоговой суммы заказа")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_orders(auth_driver):
    main_page = Items(auth_driver)
    with allure.step("Добавить товары в корзину"):
        main_page.add_item()
    with allure.step("Перейти в корзину"):
        main_page.get_in_cart()

    cart_page = Cart(auth_driver)
    with allure.step("Нажать кнопку checkout"):
        cart_page.button_checkout()

    order_page = Order(auth_driver)
    with allure.step("Заполнить форму заказа данными"):
        order_page.fill_form()
    with allure.step("Получить итоговую сумму заказа"):
        result_price = order_page.check_total_price()
    with allure.step(f"Проверка: итоговая сумма: {result_price} == $58.29"):
        assert result_price == "$58.29", \
            f"Ожидаемая сумма: $58.29, Фактическая: {result_price}"
