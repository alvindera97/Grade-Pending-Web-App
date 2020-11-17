"""
   Test suite responsible for testing unit functionalities of the institutions page
"""
from home.tests.functional_tests.main import Main


class TestLayoutOnPage(Main):
    """Test layout of institutions page"""
    def test_logo_displays_on_page(self):
        """Test logo's existence on institutions page"""
        self.get_institution_page()
        logo = self.browser.find_element_by_id('logo')
        self.assertTrue(logo.is_displayed())

    def test_header_of_the_institution_page(self):
        """Test header text's existence on institutions page"""
        self.get_institution_page()
        header_text = self.browser.find_element_by_id('header-text')
        self.assertIn("Grade Pending Calculator Institutions List", header_text.text)
        self.assertTrue(header_text.is_displayed())
