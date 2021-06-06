import selenium
from selenium.webdriver.common.by import By

from PageObject.shoppage import Shopage


class Homepage():
        def __init__(self,driver):
                self.driver=driver


        shop=(By.LINK_TEXT,"Shop")


        def goto_shop(self):
                self.driver.find_element(*Homepage.shop).click()
                shops = Shopage(self.driver)
                return shops





        





