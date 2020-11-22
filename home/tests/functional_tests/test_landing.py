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

        # "Grade Pending Calculator | Calculate Your Gp in a matter of seconds
        # with our grade pending calculator. It's fast, easy and reliable."
        welcome_text = self.browser.find_element_by_id("welcome-text")
        self.assertEqual(welcome_text.text, """Calculate your GP in a matter of seconds with our  
         grade pending calculator. It's fast, easy and reliable.""")
        self.assertGreater(len(welcome_text.text), 110)
        self.assertEqual(self.browser.title, site_main_title)

        # There is also an instructions button.
        instructions_button = self.browser.find_element_by_link_text('INSTRUCTIONS')
        # He clicks on it
        instructions_button.click()
        # and he views that the institutions button takes him to an institutions page as noted by
        # the trailing slash at the end of the link
        self.assertEqual(self.browser.current_url, self.live_server_url + '/instructions/')

    def test_login_button(self):
        """Test if the home page button is functional"""
        # James is however attracted to the text at the bottom of the screen
        # asking if he already had an account:
        have_account_text = self.browser.find_element_by_id("already-have-account-text")
        self.assertEqual(have_account_text.text, "Already have an account?")
        login_button = self.browser.find_element_by_link_text("Login")
        # he doesn't have an account, however, he clicks the login button and
        # ignores the huge "REGISTER" button
        login_button.click()
        home_page_button = self.browser.find_element_by_id('login-button')
        # He decides to click on the loin button
        home_page_button.click()
        # He can see from the login button that he is being directed to the
        # login page because of the trailing
        # /login/ in the browser URL.
        self.assertEqual(self.browser.current_url, self.live_server_url + '/login/')
        self.assertIn('login', self.browser.title)
        # satisfied that he actually reached the login page, he returns ot the lading page
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.title, site_main_title)

    def test_register_button(self):
        """Test if the home page button is functional"""
        # James is now back at the home page and proceeds to check the 'register button'
        home_page_button = self.browser.find_element_by_id('register-button')
        # He clicks the register button
        home_page_button.click()
        # After clicking the button, he is directed to the sign up page as he can see from the
        # end of the URL pointing towards the sign up page '/signup/'
        self.assertEqual(self.browser.current_url, self.live_server_url + '/signup/')

    def test_institutions_link(self):
        """Test if the institutions button directs to the institutions page"""
        # James is back at the home page
        # sets his sights on the institutions underlined link
        institutions_link = self.browser.find_element_by_id('institutions-button')
        # He clicks on the link
        institutions_link.click()
        # after clicking the link, he is redirected to the registration page
        self.assertEqual(self.browser.current_url, self.live_server_url + '/institutions/')
        # while he is on the page, he ascertains that he is on the
        # institutions page as hinted on the title of the page
        self.assertIn("Institutions", self.browser.title)
