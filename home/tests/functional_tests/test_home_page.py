"""
   Test suite responsible for testing unit functionalities of the home page
"""

from .main import Main, site_main_title


class TestHomePage(Main):
    """Home page unit tests."""

    def setUp(self) -> None:
        super().setUp()  # same as: super(TestHomePage, self).setUp()
        self.get_home_page()

    def test_home_page_title(self):
        """Home page title test"""
        # James hears of this new website, it's known as a universal grade pending calculator
        # He opens the page and he sees that the page title self-explains the purpose of the website
        # The title of the page (or home page) reads:
        # "Grade Pending Calculator | Calculate Your Gp And Cgpa In Seconds"
        self.assertEqual(self.browser.title, site_main_title)

    def test_login_button(self):
        """Test if the home page button is functional"""
        # James is however confronted with 3 buttons that clearly spell out
        # "Login", "Register" and "Institutions"
        home_page_button = self.browser.find_element_by_id('login-button')
        # He decides to click on the loin button
        home_page_button.click()
        # He can see from the login button that he is being directed to the
        # login page because of the trailing
        # /login/ in the browser URL.
        self.assertEqual(self.browser.current_url, self.live_server_url + '/login/')

    def test_register_button(self):
        """Test if the home page button is functional"""
        # James is now back at the home page and proceeds to check the 'register button'
        home_page_button = self.browser.find_element_by_id('register-button')
        # He clicks the register button
        home_page_button.click()
        # After clicking the button, he is directed to the sign up page as he can see from the
        # end of the URL pointing towards the sign up page '/signup/'
        self.assertEqual(self.browser.current_url, self.live_server_url + '/signup/')

    def test_institutions_button(self):
        """Test if the institutions button directs to the institutions page"""
        # James is back at the home page
        self.get_home_page()
        # sets his sights on the institutions button
        institutions_button = self.browser.find_element_by_id('institutions-button')
        # He clicks on the button
        institutions_button.click()
        # after clicking the button, he is redirected to the registration page
        self.assertEqual(self.browser.current_url, self.live_server_url + '/institutions/')
        # while he is on the page, he ascertains that he is on the
        # institutions page as hinted on the title of the page
        self.assertIn("Institutions", self.browser.title)
