import logging
import allure

from pages.HomePage.popup.add_bank_details import HomePopupPage
from pages.LoginPage.loginDetails_page.login_and_logout import LoginPage

log = logging.getLogger(__name__)

@allure.severity(allure.severity_level.NORMAL)
class TestStartRealWorld:
    """ This class contains create account details of real wolrd app"""

    def test_add_bank_deatils(self, init_page):
        """
        ======== Steps to add bank deatils initially ========
        1. After login, First time enter bank deatils on popup page
        2. Save it.
        **** Click Logout if user already added bank details ****
        """
        login = LoginPage(init_page)
        sigin_page = login.login()
        assert sigin_page, "SingIn error"

        #get start with real world app
        acct_page = HomePopupPage(init_page)
        acct_details = acct_page.add_bank_acct_details()
        assert acct_details

