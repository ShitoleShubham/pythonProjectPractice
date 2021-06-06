from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", default="chrome", action='store')



@pytest.fixture(scope="class")
def setup(request):
    browername=request.config.getoption("browser_name")
    if browername== "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\Mr.PerSeCuToR\\PycharmProjects\\chromedriver.exe")
    elif browername== "firefox":
        GG=baseclass()
        log=GG.getlogger()
        log.warning("we dont have firefox")
        assert False
#    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()






