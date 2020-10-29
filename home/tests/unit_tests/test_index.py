from .main import Main, site_main_title


class HomePageTest(Main):
    """Home page index page test"""
    def setUp(self) -> None: pass

    def tearDown(self) -> None: pass

    def test_home_page_title(self):
        """test home page title"""
        response = self.client.get('/')
        self.assertIn(site_main_title, response.content.title().decode())
