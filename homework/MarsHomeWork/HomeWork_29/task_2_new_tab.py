from playwright.sync_api import Page, expect, BrowserContext


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    btn = page.get_by_role('link', name='Click')
    with context.expect_page() as new_tab:
        btn.click()
    new_tab = new_tab.value
    result_text = new_tab.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    expect(btn).to_be_enabled()
