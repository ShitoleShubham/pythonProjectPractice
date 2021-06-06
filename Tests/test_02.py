
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.baseclass import BaseClass
import pytest
from testdata import websitestest



@pytest.mark.parametrize("webpage",websitestest.websites.website)
class Test_02(BaseClass):

    def test_websites(self,webpage):
        self.driver.get(webpage)
        log = self.getlogger()
        log.critical("test executed successfully")
        log.info("webpage successfully opened")
        print("GG")



