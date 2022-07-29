from selenium.webdriver.common.by import By

class pageCart:

    btn_checkout_xpath = "//button[@id='checkout']"

    def __init__(self,driver):
        self.driver = driver

    def clik_checkout(self):
        self.driver.find_element(By.XPATH, self.btn_checkout_xpath).click()