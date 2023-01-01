class PageObject:
    url = "/"

    def __init__(self, context):
        page, live_server = context
        self.page = page
        self.live_server = live_server

    def navigate(self):
        self.page.goto(f"{self.live_server.url}{self.url}")

    def check(self):
        assert self.page.url == f"{self.live_server.url}{self.url}"


class HomePage(PageObject):
    url = "/"


class SignupPage(PageObject):
    url = "/accounts/signup/"

    def __init__(self, context):
        super().__init__(context)

        page, live_server = context
        self.email_input = page.locator("#id_email")
        self.password_input = page.locator("#id_password1")
        self.terms_checkbox = page.locator("#id_terms_accepted")
        self.submit_button = page.locator("form button")

    def signup(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.terms_checkbox.check()
        self.submit_button.click()


class LoginPage(PageObject):
    url = "/accounts/login/"

    def __init__(self, context):
        super().__init__(context)

        page, live_server = context
        self.email_input = page.locator("#id_login")
        self.password_input = page.locator("#id_password")
        self.submit_button = page.locator("form button")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()


class SettingsPage(PageObject):
    url = "/accounts/settings/"

    def __init__(self, context):
        super().__init__(context)

        page, live_server = context
        self.logout_button = page.locator("#form_logout button")

    def logout(self):
        self.logout_button.click()
