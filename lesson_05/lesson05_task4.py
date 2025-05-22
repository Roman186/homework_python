from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")
Username_element = driver.find_element('xpath', '//input[@id="username"]')
Username_element.send_keys("tomsmith")
Password_element = driver.find_element('xpath', '//input[@id="password"]')
Password_element.send_keys("SuperSecretPassword!")
Login_button = driver.find_element('xpath', '//button[@type="submit"]')
Login_button.click()
Text = driver.find_element('xpath', '//div[@class="flash success"]').text
print(Text)
driver.quit()
