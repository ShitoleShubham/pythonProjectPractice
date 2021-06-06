from datetime import time

import selenium
from selenium.webdriver.common.by import By


class Shopage():
    def __init__(self, driver):
        self.driver = driver

    mobil = (By.XPATH, "//div[@class='card h-100']")

    def selectphone(self, phone):
        print(self.driver.find_elements_by_xpath("//div[@class='card h-100']/div/h4/a")[1].text)
        mobiles = self.driver.find_elements(*Shopage.mobil)
        for mobi in mobiles:
            print(mobi.find_element_by_xpath("div/h4/a").text)
            if mobi.find_element_by_xpath("div/h4/a").text == phone:
                mobi.find_element_by_xpath("div/button").click()
                print("Iphone")
            else:
                print("GG")