from .main import Main, site_main_title


class LoginPageTest(Main):
    def test_login_page_loads(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(site_main_title, response.content.title().decode())
