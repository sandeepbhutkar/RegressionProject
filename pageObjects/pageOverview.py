from selenium.webdriver.common.by import By

class pageOverview:

    value1 = "//div[@class='summary_value_label']"

    def __init__(self,driver):
        self.driver = driver

    def get_employee_id(self):
        self.var = self.driver.find_element(By.XPATH, self.value1).text
        return self.var

