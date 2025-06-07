import pytest
from selenium import webdriver
from authPage import Authorization
from main_shopPage import Items
from shop_cart_Page import Cart
from shop_orderPage import Order


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def auth_driver(driver):
    driver.get("https://www.saucedemo.com")
    auth_page = Authorization(driver)
    auth_page.auth()
    return driver


def test_auth(driver):
    driver.get("https://www.saucedemo.com")
    auth_page = Authorization(driver)
    auth_page.auth()


def test_add_items(auth_driver):
    main_page = Items(auth_driver)
    main_page.add_item()
    main_page.get_in_cart()


def test_cart_shop(auth_driver):
    main_page = Items(auth_driver)
    main_page.add_item()
    main_page.get_in_cart()

    cart_page = Cart(auth_driver)
    count_result = cart_page.count_items()
    assert count_result == 3, \
        f"Число товаров должно быть 3, в итоге: {count_result}"

    items_result = cart_page.added_items()
    expected_items = ["Sauce Labs Backpack",
                      "Sauce Labs Bolt T-Shirt",
                      "Sauce Labs Onesie"]
    assert items_result == expected_items, \
        "Названия добавленных товаров \
        не совпадает с названиями товаров в корзине"

    cart_page.button_checkout()


def test_btn_checkout(auth_driver):
    main_page = Items(auth_driver)
    main_page.add_item()
    main_page.get_in_cart()

    btn = Cart(auth_driver)
    btn.button_checkout()


def test_orders(auth_driver):
    main_page = Items(auth_driver)
    main_page.add_item()
    main_page.get_in_cart()

    cart_page = Cart(auth_driver)
    cart_page.button_checkout()

    order_page = Order(auth_driver)
    order_page.fill_form()

    result_price = order_page.check_total_price()
    assert result_price == "$58.29", \
        f"Ожидаемая сумма: $58.29, Фактическая: {result_price}"
