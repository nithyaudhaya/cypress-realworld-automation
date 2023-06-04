import logging
import time

from selenium.webdriver.common.keys import Keys


from pages.portal import Portal
from pages.LoginPage.locators import LoginLocators, LoginInfo


log = logging.getLogger(__name__)

class LoginPage(Portal):
    """This class contains functionality of the testcases """

    def __init__(self, browser):
        self.browser = browser
        self.portal = Portal(self.browser)

    def login(self):
        """
        Login the Application
        """
        try:
            log.info(f"user login as {LoginInfo.username}")
            self.send_text(LoginLocators.USERNAME, LoginInfo.username)
            self.send_text(LoginLocators.PASSWORD, LoginInfo.password)
            log.info("Click SingIn button")
            self.click(LoginLocators.SIGNIN_BTN)
            if 'signin' in self.browser.current_url:
                log.info(f"{self.browser.current_url}")
                log.info('Invalid username and Password')
                self.sign_up()
            else:
                log.info(f"Successfully login the App")
            return self
        except Exception:
            log.info("Invalid username and Password, \
                     Please Enter valid credential Or Create a new account")
            return self

    def sign_up(self):
        """
        Create new account
        """
        try:
            log.info("Sign Up page")
            signup = self.get_wait(LoginLocators.SIGNUP_LINK_TEXT).wait_for_clickable()
            signup.send_keys(Keys.ENTER)

            log.info("Enter signup details")
            self.send_text(LoginLocators.FIRST_NAME, LoginInfo.firstname)
            self.send_text(LoginLocators.LAST_NAME, LoginInfo.lastname)
            self.send_text(LoginLocators.USERNAME, LoginInfo.username)
            self.send_text(LoginLocators.PASSWORD, LoginInfo.password)
            self.send_text(LoginLocators.CONFIRM_PASSWORD, LoginInfo.confirm_password)
            log.info("Click Sign up sumbit button")
            self.click(LoginLocators.SIGNUP_SUBMIT_BTN)
            log.info(f"Successfully created a new account- username: {LoginInfo.username}")
            if 'signin' in self.browser.current_url:
                self.login()
            else:
                log.info(f"worng page. Expected Page : {self.browser.current_url}")
            return self

        except:
            log.info("Unable to create a account")

    def logout(self):
        """
        Logout the Application
        """
        log.info("Click Logout")
        self.click(LoginLocators.LOGOUT)
        if 'signin' in self.browser.current_url:
            log.info("Successfully Logout the App")
        else:
            log.info("Unable to Logout the App")




