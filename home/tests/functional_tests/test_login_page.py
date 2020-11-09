"""
   Test suite responsible for testing unit functionalities of the login page
"""

from .main import Main, site_main_title


class TestLoginPage(Main):
    def setUp(self) -> None:
        super(TestLoginPage, self).setUp()
        self.live_login_url = self.live_server_url + '/login/'

    def get_login_page(self):
        self.browser.get(self.live_login_url)

    def test_login_page_displays_at_login_url(self):
        self.get_login_page()
        self.assertIn(site_main_title, self.browser.title)

    def test_already_have_an_account_link(self):
        self.get_login_page()
        already_have_an_account_link = self.browser.find_element_by_id("if-account-link")
        already_have_an_account_link.click()
        self.assertEqual(self.browser.current_url, self.live_server_url + '/signup/')
