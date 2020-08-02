from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".bx_login_top_inline_link")

class LoginPageLocators():
    EMAIL_AUTH = (By.CSS_SELECTOR, "#email_auth")
    LOGIN_INPUT = (By.CSS_SELECTOR, '#USER_LOGIN')
    PASS_INPUT = (By.CSS_SELECTOR, '#USER_PASSWORD')
    AUTH_BUTTON = (By.CSS_SELECTOR, '.email-login__send')
