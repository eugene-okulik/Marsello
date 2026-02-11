from playwright.sync_api import expect
from test_UI_husnut_pw.pages.base_page import MainPage


class QaPracticeInputText(MainPage):
    base_url = 'https://www.qa-practice.com/elements/input/simple'

    def input_text(self, text):
        input_text = self.page.locator('#id_text_string')
        input_text.fill(text)
        input_text.press('Enter')

    def check_result_input_text(self, text):
        result_text = self.page.locator('#result-text')
        expect(result_text).to_have_text(text)
