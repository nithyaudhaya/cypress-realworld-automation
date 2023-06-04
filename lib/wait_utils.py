import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class BroweserWait:

    def __init__(self, driver, element):
        self.browser = driver
        self.element = element

    def wait_for_clickable(self, time=30):
        wait = WebDriverWait(self.browser, time)
        return wait.until(EC.element_to_be_clickable(self.element))

    def wait_for_displayed(self, time=30):
        wait = WebDriverWait(self.browser, time)
        return wait.until(EC.visibility_of_element_located(self.element))
