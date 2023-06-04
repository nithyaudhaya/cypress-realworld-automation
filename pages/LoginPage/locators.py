from selenium.webdriver.common.by import By

class LoginLocators:

    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH,"//input[@id='lastName']")
    USERNAME = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD = (By.XPATH,"//input[@id='confirmPassword']")
    SIGNIN_BTN = (By.XPATH, "//button[@data-test='signin-submit']")
    SIGNUP_LINK_TEXT = (By.LINK_TEXT, "Don't have an account? Sign Up")
    SIGNUP_SUBMIT_BTN = (By.XPATH,"//button[@data-test='signup-submit']")
    LOGOUT = (By.XPATH, "//div[@data-test='sidenav-signout']")

