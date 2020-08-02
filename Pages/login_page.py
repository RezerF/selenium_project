from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators, MainPageLocators

class LoginPage(BasePage):

    def go_to_reg_form(self):
        auth_email_link = self.browser.find_element(*LoginPageLocators.EMAIL_AUTH)
        auth_email_link.click()

    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_email_input()
        self.should_be_pass_input()
        self.should_be_button_submit()
        self.should_be_login_url()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'

    def should_be_email_input(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT), 'Login input is not present'

    def should_be_pass_input(self):
        assert self.is_element_present(*LoginPageLocators.PASS_INPUT), 'Pass input is not present'

    def should_be_button_submit(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_BUTTON), 'Button submit is not present'

    def should_be_login_url(self):
        assert 'login' in (self.browser.current_url), 'Link without "login" in url'
