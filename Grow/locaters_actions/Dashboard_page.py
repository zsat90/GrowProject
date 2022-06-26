from locaters_actions.navigate_to_url import NavigateUrl


# Objects for Dashboard page
class DashboardPageObjects(NavigateUrl):
    sales_dash_header = "//div[@id='root']/div[2]/div[2]/div/div/div/div/h1"
    sales_dash_first_tile = "//div[@id='metricTiles']/div[1]"
    expand_view_button = "//div[@id='metricTiles']/div/div/div[2]/div[2]/div/div"
    expanded_view_header = "//div[(text() = 'View' or . = 'View')]"
    expanded_raw_data = "//div[(text() = 'Raw Data' or . = 'Raw Data')]"
    expanded_chart_data = "//div[(text() = 'Chart Data' or . = 'Chart Data')]"
    expanded_view_chart = "//div[(text() = 'Chart' or . = 'Chart')]"
    expanded_chart = "//div[@id='root']/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]"
    exit_expanded_view_button = "#root > div.dashboard---dashboard---d2jjC > " \
                                "div.expandedMetric---dialogWrapper---JUjDJ > " \
                                "div.expandedMetric---dialogContent---zXnru > div.expandedMetric---container---sWJpG " \
                                "> div.topBar---topBar---ZYFQI > div.topBar---rightSide---r3LPC > " \
                                "div.topBar---closeButton---ZNR0f.STATIC-dashboard-expandedMetric-closeExpandedMetric " \
                                "> svg "
    three_dot_menu = "//div[@id='metricTiles']/div/div/div[2]/div[3]/div/div"
    copy_dashboard_option = "(.//*[normalize-space(text()) and normalize-space(.)='Created with Sketch.'])[" \
                            "1]/following::div[2] "
    second_dash_header = "//h1[(text() = 'Second Dash' or . = 'Second Dash')]"
    delete_dash_button = "//*/text()[normalize-space(.)='Delete']/parent::*"
    confirm_dash_delete_button = "//button[@type = 'button' and (text() = 'Delete' or . = 'Delete')]"
    deleted_dash_toast = "//div[@class = 'toaster---toastContainer---HqXYC toast-success' and (text() = 'Successfully " \
                         "deleted metric!' or . = 'Successfully deleted metric!')] "
    dash_menu_button = "//div[@class = 'batmanBar---menuIconContainer---gVbwN pointDown " \
                       "STATIC-dashboard-BatmanBar-toggleMenuIcon'] "
    sales_dash_menu_option = "//span[@class = 'sidebar---dashboardName---e3MZh " \
                             "STATIC-dashboard-sidebar-goToDashboard' and (text() = 'Sales Dash' or . = 'Sales Dash')] "
    second_dash_menu_option = "//span[@class = 'sidebar---dashboardName---e3MZh " \
                              "STATIC-dashboard-sidebar-goToDashboard' and (text() = 'Second Dash' or . = 'Second " \
                              "Dash')] "
    second_dash_first_tile = "//div[@class = 'metricTile---inner---hqjlt STATIC-dashboard-metric-expandMetric " \
                             "metricTile---clickableMetric---lTViM'] "
    second_dash_tile_name = "//*[@class = 'metricTitle---title---Kgu83' and (text() = 'Copy of Sales past 60 days by " \
                            "rep' or . = 'Sales past 60 days by rep')] "


# Actions for Dashboard page
class DashboardPageActions(DashboardPageObjects):
    def click_expand_view(self):
        self.click(self.expand_view_button)

    def exit_expanded_view(self):
        self.click(self.exit_expanded_view_button)

    def hover_over_card(self):
        self.hover_on_element(self.sales_dash_first_tile)

    def click_three_dot_menu(self):
        self.click(self.three_dot_menu)

    def click_copy_dashboard(self):
        self.click(self.copy_dashboard_option)

    def click_delete_dash_button(self):
        self.click(self.delete_dash_button)

    def click_confirm_delete(self):
        self.click(self.confirm_dash_delete_button)

    def click_dash_menu_button(self):
        self.click(self.dash_menu_button)

    def click_sales_dash_menu_item(self):
        self.click(self.sales_dash_menu_option)