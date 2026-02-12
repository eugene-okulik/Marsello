from test_UI_husnut_pw.pages.base_page import MainPage


class DemoQa(MainPage):
    base_url = 'https://demoqa.com/automation-practice-form'

    def filling_form(self):
        input_name = self.page.get_by_placeholder('First Name')
        input_name.fill('Shrek')

        input_last_name = self.page.get_by_placeholder('Last Name')
        input_last_name.fill('Boloto')

        input_mail = self.page.get_by_placeholder('name@example.com')
        input_mail.fill('name@example.com')

        gender = self.page.locator("[for = 'gender-radio-1']")
        gender.click()

        input_mobile = self.page.get_by_placeholder('Mobile Number')
        input_mobile.fill('1111111111')

        input_birth_day = self.page.locator('#dateOfBirthInput')
        input_birth_day.fill('20 Nov 2000')

        input_subjects = self.page.locator('#subjectsInput')
        input_subjects.fill('Hindi')
        input_subjects.press('Enter')

        hobby = self.page.locator('[for="hobbies-checkbox-1"]')
        hobby.click()

        input_address = self.page.get_by_placeholder('Current Address')
        input_address.fill('Grove Street')

        state_input = self.page.locator('#react-select-3-input')
        state_input.fill("NCR")
        state_input.press('Enter')

        city_input = self.page.locator('#react-select-4-input')
        city_input.fill("Delhi")
        city_input.press('Enter')

        submit_button = self.page.get_by_text('Submit')
        submit_button.click()

    def check_result_form(self):
        result = self.page.locator(".modal-dialog").inner_text()
        print(result)
