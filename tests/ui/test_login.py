import logging

from pages.LoginPage.loginDetails_page.login_and_logout import LoginPage

log = logging.getLogger(__name__)

class TestLogin:

    def test_create_new_account(self, init_page):
        """
        ======== Steps to create new account ========
        1. Click SingUp link on Login Page
        2. Enter all details and click submit
        """
        log.info("Create new account")
        login = LoginPage(init_page)
        signup = login.sign_up()
        assert signup, "SingUp error"

    def test_user_login(self, init_page):
        """
        ======== Steps to login the application ========
        1. Click SingIn page
        2. Enter Registered username and password and submit
        """
        log.info("User Login")
        login = LoginPage(init_page)
        landing = login.login()
        assert landing, "Signin error"





