import pytest

from tests.core.fixtures.defaults import DEFAULT_EMAIL, DEFAULT_PASSWORD

from .page_objects import HomePage, LoginPage, SettingsPage, SignupPage


@pytest.mark.ui
@pytest.mark.db(transaction=True)
def test_user_signup_login_logout_scenario(page, live_server):
    context = (page, live_server)
    signup = SignupPage(context)
    signup.navigate()
    signup.signup(DEFAULT_EMAIL, DEFAULT_PASSWORD)
    home = HomePage(context)
    home.check()
    settings = SettingsPage(context)
    settings.navigate()
    settings.logout()
    home.check()
    login = LoginPage(context)
    login.navigate()
    login.login(DEFAULT_EMAIL, DEFAULT_PASSWORD)
    home.check()
    settings.navigate()
    settings.logout()
