"""
   Test suite responsible for testing unit functionalities of the institutions page
"""
from django.test import override_settings

from .main import Main


@override_settings(DEBUG=True)
class TestInstitutionsPage(Main):
    """Test suite for the institutions page as viewed from the homepage"""
    def test_institution_page_loads(self):
        self.get_institution_page()
        self.assertIn("Institutions", self.browser.title)

    def test_logo_displays_on_page(self):
        self.get_institution_page()
        logo = self.browser.find_element_by_id('logo')
        self.assertTrue(logo.is_displayed())

    def test_header_of_the_institution_page(self):
        self.get_institution_page()
        header_text = self.browser.find_element_by_id('header-text')
        self.assertIn("Grade Pending Calculator Institutions List", header_text.text)
        self.assertTrue(header_text.is_displayed())
