from playwright.sync_api import expect
from test_UI_husnut_pw.pages.base_page import MainPage


class QaPracticeLanguageSelection(MainPage):
    base_url = 'https://www.qa-practice.com/elements/select/single_select'
    language_name = None
    language = None

    def language_selection(self, selected_language):
        drop_down = self.page.locator('[name="choose_language"]')
        drop_down.click()

        self.language = self.page.locator('select[name="choose_language"]')
        self.language.select_option(selected_language)
        self.language_name = self.language.inner_text()

        button = self.page.locator('[class="btn btn-primary"]')
        button.click()

    def check_result_input_text(self):
        result = self.page.locator('#result-text').inner_text()
        expect(self.language).to_contain_text(result)
