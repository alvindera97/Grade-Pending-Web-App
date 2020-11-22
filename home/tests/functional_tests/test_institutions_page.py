"""
   Test suite responsible for testing unit functionalities of the institutions page
"""

from .main import Main


class TestInstitutionsPage(Main):
    """Test suite for the institutions page as viewed from the homepage"""
    def test_institutions_page_loads(self):
        """Test if institution page loads from Home Page"""
        self.get_landing_page()
        institutions_page_button = self.browser.find_element_by_id("institutions-button")
        institutions_page_button.click()
        self.assertIn("Institutions", self.browser.title)
