import time
import logging

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException

from lib.wait_utils import BroweserWait

log = logging.getLogger(__name__)

class Portal:
    """ This file contains custome function for send_keys, click """

    def __init__(self, browser):
        self.browser = browser

    def get_wait(self, element=None):
        return BroweserWait(self.browser, element)

    def click(self, locator):
        attempts = 5
        while attempts != 0:
            try:
                element = self.get_wait(locator).wait_for_clickable()
                element.click()
                time.sleep(2)
                break
            except (StaleElementReferenceException, \
                    ElementClickInterceptedException, ElementNotInteractableException):
                time.sleep(2)
                attempts = attempts - 1
                log.info(f'{locator} element became stale, {attempts} attempts remaining')

    def send_text(self, locator, value):
        self.get_wait(locator).wait_for_clickable()
        self.browser.find_element(*locator).send_keys(Keys.CONTROL + 'a')
        self.browser.find_element(*locator).send_keys(Keys.DELETE)
        self.browser.find_element(*locator).send_keys(value)

    def is_element_present(self, element):
        try:
            self.browser.find_element(*element)
            return True
        except NoSuchElementException:
            return False


