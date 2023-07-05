from pages.base_page import BasePage


class LoginPage(BasePage):
    scouts_panel_heading_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button/span[1]"
    polski_button_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
