from wagtail.core.models import Page


class HomePage(Page):
    """Page object for the home page"""
    template = 'home/home.html'
