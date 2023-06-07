"""
This file contains locators and functions for elements of PopUp Page of after login
"""
import logging

from pages.HomePage.locators import AddBankDetails, BankDetailsInfo
from pages.LoginPage.loginDetails_page.login_and_logout import LoginPage
from pages.portal import Portal

log = logging.getLogger(__name__)

class HomePopupPage(Portal):
    """
    Class for locators and function for elements of Home page of Popup to add bank deatils
    """

    def __init__(self, browser):
        self.browser = browser
        self.portal = Portal(self.browser)
        self.LoginPage = LoginPage(self.browser)

    def add_bank_acct_details(self):
        """
        This function for check and Add bank account details
        """
        element = self.is_element_present(AddBankDetails.REAL_WORLD_APP_POPUP_HEADER)
        if element:
            try:
                log.info("Add account details")
                log.info("Click Next button")
                self.click(AddBankDetails.NEXT_BTN)
                log.info("Enter bank details")
                self.send_text(AddBankDetails.BANK_NAME, BankDetailsInfo.input_bank_name)
                self.send_text(AddBankDetails.ROUTING_NUMBER, BankDetailsInfo.input_routing_number)
                self.send_text(AddBankDetails.ACCOUNT_NUMBER, BankDetailsInfo.input_ac_number)
                self.click(AddBankDetails.SAVE_BTN)
                self.click(AddBankDetails.DONE_BTN)
                log.info("Successfully entered bank details")
                self.LoginPage.logout()
                return self
            except Exception as e:
                log.info(e)
        else:
            log.info("Account details are alreday added")
            self.LoginPage.logout()
            return self

