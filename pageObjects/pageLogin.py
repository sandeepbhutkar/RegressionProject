from selenium import webdriver
from selenium.webdriver.common.by import By

class pageLogin:
    txt_username_xpath = "//input[@name='user-name']"
    txt_password_xpath = "//input[@id='password']"
    btn_login_xpath = "//input[@class='submit-button btn_action']"

    def  __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, user_name):
          self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys(user_name)

    def enter_password(self, password):
          self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def click_login_button(self):
          self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
