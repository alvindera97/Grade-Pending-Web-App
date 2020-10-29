from .main import Main


class TestHomePage(Main):
    def test_smoking_gun(self):
        self.assertEqual(1 + 1, "asa")
