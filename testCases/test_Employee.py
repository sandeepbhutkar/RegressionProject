from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.pageLogin import pageLogin
from pageObjects.pageProduct import pageProduct
from pageObjects.pageCart import pageCart
from pageObjects.pageCheckout import pageCheckout
from pageObjects.pageOverview import pageOverview
from utilities import XLutils
class Test_Employee:
    def test_employee(self):
        self.path = "C:/Users/sbhutkar/PycharmProjects/RegressionProject/testData/TestData.xlsx"
        self.rows = XLutils.get_row_count(self.path, "Sheet1")
        for r in range(2, self.rows + 1):
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.get("https://www.saucedemo.com/")
            # Login Page
            self.pl = pageLogin(self.driver)
            self.pl.enter_user_name(XLutils.read_data(self.path, "Sheet1", r, 2))
            self.pl.enter_password(XLutils.read_data(self.path, "Sheet1", r, 3))
            self.pl.click_login_button()
            # Products Page
            self.pp = pageProduct(self.driver)
            self.pp.click_add_to_cart_button()
            self.pp.click_cart()
            # Cart Page
            self.pc = pageCart(self.driver)
            self.pc.clik_checkout()
            # Checkout Page
            self.pc = pageCheckout(self.driver)
            self.pc.enter_firstname(XLutils.read_data(self.path, "Sheet1", r, 4))
            self.pc.enter_lastname(XLutils.read_data(self.path, "Sheet1", r, 5))
            self.pc.enter_postalcode(XLutils.read_data(self.path, "Sheet1", r, 6))
            self.pc.click_continue_button()
            # Overview Page
            self.po = pageOverview(self.driver)
            val = self.po.get_employee_id()
            XLutils.write_data(self.path, "Sheet1", r, 7, val)
            time.sleep(3)
            self.driver.close()


