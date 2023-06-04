import time
import logging

from selenium.webdriver import ActionChains
from lib.wait_utils import BroweserWait
from selenium.webdriver.common.keys import Keys

log = logging.getLogger(__name__)

class Portal:
    def __init__(self, browser):
        self.browser = browser

    def get_wait(self, element=None):
        return BroweserWait(self.browser, element)




