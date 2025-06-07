class Authorization:
    def __init__(self, driver):
        self.driver = driver

    def auth(self):
        (self.driver.find_element
         ("xpath", "//input[@id='user-name']").send_keys("standard_user"))
        (self.driver.find_element
         ("xpath", "//input[@id='password']").send_keys("secret_sauce"))
        (self.driver.find_element
         ("xpath", "//input[@id='login-button']").click())
