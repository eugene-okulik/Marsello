from time import sleep
from playwright.sync_api import Page


def test_input_text(page: Page):
    page.goto("https://demoqa.com/automation-practice-form", wait_until="domcontentloaded")
    input_name = page.get_by_placeholder('First Name')
    input_name.fill('Shrek')

    input_last_name = page.get_by_placeholder('Last Name')
    input_last_name.fill('Boloto')

    input_mail = page.get_by_placeholder('name@example.com')
    input_mail.fill('name@example.com')

    gender = page.locator("[for = 'gender-radio-1']")
    gender.click()

    input_mobile = page.get_by_placeholder('Mobile Number')
    input_mobile.fill('1111111111')

    input_birth_day = page.locator('#dateOfBirthInput')
    input_birth_day.fill('20 Nov 2000')

    input_subjects = page.locator('#subjectsInput')
    input_subjects.fill('Hindi')
    input_subjects.press('Enter')

    hobby = page.locator('[for="hobbies-checkbox-1"]')
    hobby.click()

    input_address = page.get_by_placeholder('Current Address')
    input_address.fill('Grove Street')

    state_input = page.locator('#react-select-3-input')
    state_input.fill("NCR")
    state_input.press('Enter')

    city_input = page.locator('#react-select-4-input')
    city_input.fill("Delhi")
    city_input.press('Enter')

    submit_button = page.get_by_text('Submit')
    submit_button.click()
