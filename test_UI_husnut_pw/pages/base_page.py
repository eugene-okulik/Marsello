from playwright.sync_api import Page


class MainPage:
    base_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f'{self.base_url}', wait_until="domcontentloaded")
