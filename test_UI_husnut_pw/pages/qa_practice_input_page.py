from playwright.sync_api import expect
from test_UI_husnut_pw.pages.base_page import MainPage


class QaPracticeInputText(MainPage):
    base_url = 'https://www.qa-practice.com/elements/input/simple'
    text = 'hesoyam'

    def input_text(self):
        input_text = self.page.locator('#id_text_string')
        input_text.fill(self.text)
        input_text.press('Enter')

    def check_result_input_text(self):
        result_text = self.page.locator('#result-text')
        expect(result_text).to_have_text(self.text)
