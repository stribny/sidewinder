import pytest
from playwright.sync_api import sync_playwright
from rest_framework.test import APIClient

from .core.fixtures.factories import *


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def browser():
    with sync_playwright() as p:
        for browser_type in [p.firefox]:
            browser = browser_type.launch()
            yield browser
            browser.close()


@pytest.fixture()
def page(browser):
    return browser.new_page()
