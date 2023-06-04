import pytest

from selenium import webdriver

from config.constant import ConfigURLdetails

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture(scope='module')
def init_page(driver):
    driver.get(ConfigURLdetails.URL)
    yield driver
    driver.quit()
