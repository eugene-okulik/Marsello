from playwright.sync_api import Page


def test_login_form(page: Page):
    page.goto('https://the-internet.herokuapp.com/')

    form_auth = page.get_by_role('link', name='Form Authentication')
    form_auth.click()

    user_name = page.get_by_role('textbox', name='username')
    user_name.fill('Shrek')

    passw = page.get_by_role('textbox', name='password')
    passw.fill('i_love_boloto')

    btn_login = page.get_by_role('button')
    btn_login.click()
