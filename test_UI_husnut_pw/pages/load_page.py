from playwright.sync_api import expect
from test_UI_husnut_pw.pages.base_page import MainPage


class Load(MainPage):
    base_url = 'https://the-internet.herokuapp.com/dynamic_loading/2'

    def click_and_wait(self):
        btn_start = self.page.locator('#start > button')
        btn_start.click()

        self.finish = self.page.locator('#finish')
        expect(self.finish).to_be_visible(timeout=6000)

    def check_final_text(self):
        checked_text = 'Hello World!'
        expect(self.finish).to_have_text(checked_text)
