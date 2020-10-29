""" Main tests module: main.py

    This is where all [functional] test case setup is done.
    All other test classes inherit critical performance behaviour from this module's contents
"""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium.webdriver import Chrome
from wagtail.core.models import Page, Site

from home.models import HomePage

# the reason for title() method being applied here is that
# the title attribute is titled on database save.
site_main_title: str = "Grade Pending Calculator | Calculate your GP and CGPA in seconds".title()


class Main(StaticLiveServerTestCase, TestCase):
    """Main test class.

       This class does not carry out any tests, however it contains set up
       data for the functional tests."""
    @classmethod
    def setUpClass(cls):
        # set up root page if there isn't any,
        cls.root = Page.objects.get(title="Root") if Page.objects.first() else Page.objects.create(
            title="Root",
            path="001",
            depth=1,
        )

        # set up 'Site' object if there isn't any
        cls.site = Site.objects.first() if Site.objects.first() else Site.objects.create(
            site_name="localhost",
            is_default_site=True,
            root_page=cls.root,
        )

        # Set up home page
        cls.home_page = HomePage(title=site_main_title)
        # publish the home page!
        cls.root.add_child(instance=cls.home_page).save_revision().publish()

        # don't forget to make the home page the root page of the Site object
        cls.site.root_page = cls.home_page
        cls.site.save()

        super(Main, cls).setUpClass()

    def setUp(self) -> None:
        self.browser = Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()
