

from locaters_actions.login_page import LoginActions


class NavigateUrl(LoginActions):
    def navigate_to_login(self):
        self.maximize_window()
        # navigate to url
        self.open("https://app.gogrow.com/dashboard/94980/")

        # login with correct credentials
        self.login()

        self.wait(5)



