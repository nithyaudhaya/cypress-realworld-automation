import logging
import allure

from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys


from pages.portal import Portal
from pages.LoginPage.locators import LoginLocators
from config.constant import Cypressconfig


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
            log.info(f"user login as {Cypressconfig.username}")
            self.send_text(LoginLocators.USERNAME, Cypressconfig.username)
            self.send_text(LoginLocators.PASSWORD, Cypressconfig.password)
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
            allure.attach(self.browser.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
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
            self.send_text(LoginLocators.FIRST_NAME, Cypressconfig.firstname)
            self.send_text(LoginLocators.LAST_NAME, Cypressconfig.lastname)
            self.send_text(LoginLocators.USERNAME, Cypressconfig.username)
            self.send_text(LoginLocators.PASSWORD, Cypressconfig.password)
            self.send_text(LoginLocators.CONFIRM_PASSWORD, Cypressconfig.confirm_password)
            log.info("Click Sign up sumbit button")
            self.click(LoginLocators.SIGNUP_SUBMIT_BTN)
            log.info(f"Successfully created a new account- username: {Cypressconfig.username}")
            if 'signin' in self.browser.current_url:
                self.login()
            else:
                log.info(f"worng page. Expected Page : {self.browser.current_url}")
                allure.attach(self.browser.get_screenshot_as_png(), name="testSignUpScreen",
                          attachment_type=AttachmentType.PNG)
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
            allure.attach(self.browser.get_screenshot_as_png(), name="testLogoutScreen",
                          attachment_type=AttachmentType.PNG)




