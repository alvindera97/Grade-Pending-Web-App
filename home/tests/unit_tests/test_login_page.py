from .main import Main, site_main_title


class LoginPageTest(Main):
    def test_login_page_loads(self):
        response = self.client.get('/login/')
        self.assertIn(site_main_title, response.content.title().decode())
