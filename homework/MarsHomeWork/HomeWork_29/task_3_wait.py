from playwright.sync_api import Page, expect


def test_color_change_btn(page: Page):
    page.goto('https://demoqa.com/dynamic-properties', wait_until="domcontentloaded")
    btn_visible_5sec = page.get_by_role('button', name='Visible After 5 Seconds')
    expect(btn_visible_5sec).to_be_visible(timeout=6000)
    btn_color = page.get_by_role('button', name='Color Change')
    btn_color.click()
