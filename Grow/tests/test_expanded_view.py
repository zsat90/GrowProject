from locaters_actions.Dashboard_page import DashboardPageActions


class ExpandedView(DashboardPageActions):
    def test_open_expanded_view(self):
        # goes to url and logs in
        self.navigate_to_login()

        # Verifies we are in the sales dashboard
        self.assert_element(self.sales_dash_header)

        # hovers over the first card
        self.hover_over_card()

        # clicks on the expand view button in the first card
        self.click_expand_view()

        # Verifies that the expanded view has been opened by asserting elements on that page
        self.assert_element(self.expanded_view_header)

        self.assert_element(self.expanded_raw_data)

        self.assert_element(self.expanded_chart_data)

        self.assert_element(self.expanded_view_chart)

        # closes expanded view by clicking close button
        self.exit_expanded_view()

        # Verify that the expanded view was closed
        self.assert_element_not_present(self.expanded_view_header)
