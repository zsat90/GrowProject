from seleniumbase import BaseCase
from login_info.logininfo import LoginInfo


# class that has all the login page objects
class LoginObjects(BaseCase):
    username_field = "//input[@name='email']"
    password_field = "//input[@name='password']"
    login_button = "//button[@type='submit']"
    forgot_password_button = "//form[@id='LoginForm']/div/div[3]/a"
    google_sign_up_button = "//button[@id='GoogleSignIn']"


# Actions for login page
class LoginActions(LoginObjects, LoginInfo):
    def login(self):
        self.send_keys(self.username_field, self.username)
        self.send_keys(self.password_field, self.password)
        self.click(self.login_button)
