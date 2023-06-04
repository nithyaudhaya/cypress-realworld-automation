import logging

from selenium.webdriver.common.keys import Keys

from lib.wait_utils import BroweserWait
from pages.portal import Portal

from pages.LoginPage.locators import Locators, LoginInfo


log = logging.getLogger(__name__)

class LoginPage(Portal):

    def __init__(self, driver):
        self.driver = driver

    def get_wait(self, element=None):
        return BroweserWait(self.driver, element)

    def login(self):
        """
        Login the Application
        """
        try:
            log.info(f"user login as {LoginInfo.username}")
            username_field = self.get_wait(Locators.USERNAME).wait_for_clickable()
            username_field.send_keys(LoginInfo.username)
            password_field = self.get_wait(Locators.PASSWORD).wait_for_clickable()
            password_field.send_keys(LoginInfo.password)
            log.info(f"Click SingIn button")
            self.get_wait(Locators.SIGNIN_BTN).wait_for_clickable()
            self.driver.find_element(*Locators.SIGNIN_BTN).click()
            return True
        except Exception:
            log.info("Username and Password is invalid, Please Enter valid credential Or Create a new account")
            return False

    def sign_up(self):
        """
        Create new account
        """
        try:
            log.info("Sign Up page")

            signup = self.get_wait(Locators.SIGNUP_LINK_TEXT).wait_for_clickable()
            signup.send_keys(Keys.ENTER)

            firstname_field = self.get_wait(Locators.FIRST_NAME).wait_for_clickable()
            firstname_field.send_keys(LoginInfo.firstname)
            lastname = self.get_wait(Locators.LAST_NAME).wait_for_clickable()
            lastname.send_keys(LoginInfo.lastname)
            username = self.get_wait(Locators.USERNAME).wait_for_clickable()
            username.send_keys(LoginInfo.username)
            password = self.get_wait(Locators.PASSWORD).wait_for_clickable()
            password.send_keys(LoginInfo.password)

            confirm_pwd = self.get_wait(Locators.CONFIRM_PASSWORD).wait_for_clickable()
            confirm_pwd.send_keys(LoginInfo.confirm_password)
            log.info("Click Sign up sumbit button")
            self.get_wait(Locators.SIGNUP_SUBMIT_BTN).wait_for_clickable()
            self.driver.find_element(*Locators.SIGNUP_SUBMIT_BTN).click()
            return True

        except:
            log.info("Unable to create a account")

    def logout(self):
        """
        Logout the Application
        """
        log.info("Logout")
        self.click(Locators.LOGOUT)




