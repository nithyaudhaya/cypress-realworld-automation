"""
This file contains locators and value to add bank details
"""

from selenium.webdriver.common.by import By

class AddBankDetails:
    REAL_WORLD_APP_POPUP_HEADER = \
        (By.XPATH, "//h2[normalize-space()='Get Started with Real World App']")
    NEXT_BTN = (By.XPATH, "//button[@data-test='user-onboarding-next']")
    CREATE_BANK_ACCOUNT_HEADER = (By.XPATH, "//h2[normalize-space()='Create Bank Account']")
    BANK_NAME = (By.XPATH, "//input[@id='bankaccount-bankName-input']")
    ROUTING_NUMBER = (By.XPATH, "//input[@id='bankaccount-routingNumber-input']")
    ACCOUNT_NUMBER = (By.XPATH, "//input[@id='bankaccount-accountNumber-input']")
    SAVE_BTN = (By.XPATH, "//button[@data-test='bankaccount-submit']")
    DONE_BTN = (By.XPATH, "//button[@data-test='user-onboarding-next']")

class BankDetailsInfo:
    input_bank_name = "OKHDFC"
    input_routing_number = "074000078"
    input_ac_number= "0112345678"