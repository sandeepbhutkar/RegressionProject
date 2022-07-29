from selenium.webdriver.common.by import By

class pageCheckout:

    txt_firstname_xpath = "//input[@id='first-name']"
    txt_lastname_xpath = "//input[@id='last-name']"
    txt_postalcode_xpath = "//input[@id='postal-code']"
    btn_continue_xpath = "//input[@id='continue']"

    def __init__(self, driver):
        self.driver = driver

    def enter_firstname(self,firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)

    def enter_postalcode(self, postalcode):
        self.driver.find_element(By.XPATH, self.txt_postalcode_xpath).send_keys(postalcode)

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

