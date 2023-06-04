import logging
import allure
import pytest

from pages.LoginPage.loginDetails_page.login_and_logout import LoginPage

log = logging.getLogger(__name__)

@allure.severity(allure.severity_level.NORMAL)
class TestLogin:
    """ This class contains login the app """

    @pytest.mark.skip()
    def test_create_new_account(self, init_page):
        """
        ======== Steps to create new account ========
        1. Click SingUp link on Login Page
        2. Enter all details
        3. Click submit
        **** It's return to signin page ****
        """
        log.info("Create new account")
        login = LoginPage(init_page)
        signup = login.sign_up()
        assert signup, "SingUp error"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_login(self, init_page):
        """
        ======== Steps to login the application ========
        1. Click SingIn page
        2. Enter Registered username and password
        3. Click submit
        """
        log.info("User Login")
        login = LoginPage(init_page)
        landing = login.login()
        assert landing, "Signin error"





