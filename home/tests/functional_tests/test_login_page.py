"""
   Test suite responsible for testing unit functionalities of the login page
"""
from typing import NoReturn

from .main import Main, site_main_title


class TestLoginPage(Main):
    """Login page test suite"""
    def setUp(self) -> None:
        """Defines commands to be executed before every test method"""
        super().setUp()
        self.get_login_page()

    def test_login_page_displays_at_login_url(self):
        """Test if login page displays at correct login url"""
        # Now James is at the login page
        # He checks the title of the page just to ascertain that he is still on the same site
        # He checks and sees that a large chunk of the
        # login page's title is similar to the home page's title
        self.assertIn(site_main_title, self.browser.title)
        # He also checks too see if the word "Login" is in the page's title
        self.assertIn("Login", self.browser.title)

    def test_Login_page_header(self) -> NoReturn:
        """Tests if login page has header and if it's displayed"""
        login_page_header = self.browser.find_element_by_id('login-page-header')
        expected_text = "Welcome Back"
        self.assertEqual(login_page_header, expected_text)
        self.assertTrue(login_page_header.is_displayer())

    def test_already_have_an_account_link(self):
        """Tests for text asking if user already has account"""
        # while on the login page
        # james notices that there is an instruction below the login buttons
        already_have_an_account_link = self.browser.find_element_by_id("if-account-link")
        # he clicks on the link
        already_have_an_account_link.click()
        # the link redirects him to the registration page
        self.assertEqual(self.browser.current_url, self.live_server_url + '/signup/')

    def test_finish_the_test(self):
        """The test would always fail. It is supposed to remind us to
           FINISH WRITING THE TESTS"""
        self.fail("Finish the test!")
