from selenium.webdriver.common.by import By

class pageProduct:
    btn_addtocart_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
    btn_cart_xpath = "//a[@class='shopping_cart_link']"

    def __init__(self,driver):
        self.driver = driver

    def click_add_to_cart_button(self):
        self.driver.find_element(By.XPATH, self.btn_addtocart_xpath).click()

    def click_cart(self):
        self.driver.find_element(By.XPATH, self.btn_cart_xpath).click()



