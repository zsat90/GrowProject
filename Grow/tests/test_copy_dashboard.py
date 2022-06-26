from locaters_actions.Dashboard_page import DashboardPageActions
from locaters_actions.copy_dashboard_objects import CopyDashboardActions


class CopyDashboard(DashboardPageActions, CopyDashboardActions):
    def test_copy_dashboard(self):
        # navigates to login and enter credentials
        self.navigate_to_login()

        # hovers over card to see options
        self.hover_over_card()

        # clicks three dot menu in tile
        self.click_three_dot_menu()

        # clicks the copy dashboard option
        self.click_copy_dashboard()

        # verifies that the copy options is present
        self.assert_element(self.copy_metric_header)

        # clicks the dropdown to select which dash to copy to
        self.click_select_dashboard()

        # unchecks the sales dash option so the copy won't be there
        self.click_sales_dash_option()

        # selects the second dash to copy to
        self.click_second_dash_option()

        # clicks ok after second dash was selected
        self.click_select_ok_button()

        # clicks the confirm ok button to copy the dash
        self.click_confirm_ok_button()

        # after the dash is copied it verifies it went to the second dash
        self.assert_text('Second Dash', self.second_dash_header)

        # verifies the tile was copied and is present
        self.assert_element(self.second_dash_first_tile)

        # verifies the name of the copied tile
        self.assert_text("Copy of Sales past 60 days by rep", self.second_dash_tile_name)

        self.wait(3)

        self.hover_over_card()

        # clicks on the menu and deletes the tile from the second dash and verifies it has been deleted
        self.click_three_dot_menu()

        self.click_delete_dash_button()

        self.click_confirm_delete()

        self.assert_element_not_present(self.second_dash_first_tile)

        self.wait(3)

        # returns to the sales dash and verifies the tile is still present
        self.click_dash_menu_button()

        self.click_sales_dash_menu_item()

        self.assert_element(self.sales_dash_first_tile)
