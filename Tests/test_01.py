import inspect

from selenium import webdriver
from selenium.webdriver import ActionChains
from utilities.Readconfig import Readconfigs
from PageObject.homepage import Homepage
from utilities.baseclass import BaseClass
import pytest



class TestOne(BaseClass):

    @pytest.mark.sanity
    def test_Google(self):
        #WP = Readconfigs()
        self.driver.get(Readconfigs.geturl(inspect.stack()[0][3]))
        logger=BaseClass.getlogger()
        logger.info("tests are started")

        homepages=Homepage(self.driver)
        self.driver.implicitly_wait(5)
        shop=homepages.goto_shop()
        shop.selectphone("iphone X")
        logger.info("tests completed")
        print(inspect.stack()[0][3])

