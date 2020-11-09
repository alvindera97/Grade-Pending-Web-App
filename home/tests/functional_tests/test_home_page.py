"""
   Test suite responsible for testing unit functionalities of the home page
"""

from .main import Main, site_main_title


class TestHomePage(Main):
    """Home page unit tests."""

    def setUp(self) -> None:
        super().setUp()  # same as: super(TestHomePage, self).setUp()
        self.browser.get(self.live_server_url)

    def test_home_page_title(self):
        """Home page title test"""
        self.assertEqual(self.browser.title, site_main_title)

    def test_login_button(self):
        """Test if the home page button is functional"""
        home_page_button = self.browser.find_element_by_id('login-button')
        home_page_button.click()
        self.assertEqual(self.browser.current_url, self.live_server_url + '/login/')

    def test_register_button(self):
        """Test if the home page button is functional"""
        home_page_button = self.browser.find_element_by_id('register-button')
        home_page_button.click()
        self.assertEqual(self.browser.current_url, self.live_server_url + '/signup/')
