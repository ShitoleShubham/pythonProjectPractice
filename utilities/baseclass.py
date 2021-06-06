import inspect

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def waitusingelement(self,locator):
        wait=WebDriverWait(self.driver,5)
        wait.until((expected_conditions.presence_of_element_located(By.CSS_SELECTOR, locator)))

    @staticmethod
    def getlogger():
        loggername=inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        a=logging.FileHandler(".\\logs\\logfile.log")
        a.setFormatter(logging.Formatter('%(asctime)s :%(levelname)s : %(name)s :%(message)s'))
        logger.addHandler(a)
        logger.setLevel(logging. DEBUG)

        return logger

