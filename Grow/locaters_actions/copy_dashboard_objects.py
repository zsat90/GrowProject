from seleniumbase import BaseCase


class CopyDashboardObjects(BaseCase):
    copy_metric_header = "//div[@class = 'Modal---title---BiFYN' and (text() = 'Copy Metric to Dashboard' or . = " \
                         "'Copy Metric to Dashboard')] "
    copy_success_toast = "//*[@class = 'toaster---toastContainer---HqXYC toast-success' and (text() = 'Successfully " \
                         "copied metrics!' or . = 'Successfully copied metrics!')] "
    select_dashboard_to_copy_dropdown = "//*[@type = 'text' and @placeholder = 'Select One']"

    sales_dash_dropdown_option = "//*[@class = 'DropdownOption---text---LkJsf' and (text() = 'Sales Dash' or . = " \
                                 "'Sales Dash')] "
    second_dash_dropdown_option = "//*[@class = 'DropdownOption---text---LkJsf' and (text() = 'Second Dash' or . = " \
                                  "'Second Dash')] "
    select_dash_ok_button = "//button[@class = 'Button---button---aWeP_ Button---layoutType-outline---oGPAK " \
                            "Button---styleType-regular---ALTGU Button---colorType-primary---utoL5 " \
                            "Button---small---XBGPz Dropdown---btn---ovCYz' and @type = 'button' and (text() = 'OK' or " \
                            ". = 'OK')] "
    confirm_dash_ok_button = "//button[@class = 'Button---button---aWeP_ Button---layoutType-regular---y6FUd " \
                             "Button---styleType-regular---ALTGU Button---colorType-primary---utoL5' and @type = " \
                             "'button' and (text() = 'OK' or . = 'OK')] "
    copying_metric_toast = "/div[@class = 'toaster---toastContainer---HqXYC toast-info' and (text() = 'Copying " \
                           "metric...' or . = 'Copying metric...')] "


class CopyDashboardActions(CopyDashboardObjects):
    def click_select_dashboard(self):
        self.click(self.select_dashboard_to_copy_dropdown)

    def click_sales_dash_option(self):
        self.click(self.sales_dash_dropdown_option)

    def click_second_dash_option(self):
        self.click(self.second_dash_dropdown_option)

    def click_select_ok_button(self):
        self.click(self.select_dash_ok_button)

    def click_confirm_ok_button(self):
        self.click(self.confirm_dash_ok_button)
