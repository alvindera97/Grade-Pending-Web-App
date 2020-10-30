"""Main tests module: main.py
  This is where all [unit] test case setup is done.
  All other test classes inherit critical performance behaviour from this module's contents
"""
from django.http import HttpRequest
from django.test import Client, override_settings
from wagtail.core.models import Page, Site
from wagtail.tests.utils import WagtailPageTests

from home.models import HomePage
from ..functional_tests.main import site_main_title


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class Main(WagtailPageTests):
    """Main test class.

       This class does not carry out any tests, however it contains set up
       data for the unit tests."""

    @classmethod
    def setUpTestData(cls):
        # Set up root page required if there isn't any
        cls.root = Page.objects.get(title="Root").specific if Page.objects.count() > 0 else Page.objects.create(
            title="Root",
            path="001",
            depth=1,
        )

        # Set up home page and make it child of root page
        cls.home_page = HomePage(title=site_main_title)
        cls.root.add_child(instance=cls.home_page).save_revision().publish()

        # set up Site object if there isn't any
        cls.site = Site.objects.first() if Site.objects.first().site_name == "localhost" else Site.objects.create(
            site_name="localhost",
            is_default_site=True,
            root_page=cls.home_page,
        )

        cls.site.root_page = cls.home_page  # watch for necessity
        cls.site.save()  # watch for necessity

        super(Main, cls).setUpTestData()

    def setUp(self):
        self.request = HttpRequest()
        self.client = Client()
