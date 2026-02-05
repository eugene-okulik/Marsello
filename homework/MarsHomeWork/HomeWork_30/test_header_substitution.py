from playwright.sync_api import Page, expect, Route
import re
import json

phone_name = 'яблокофон 17 про'


def test_iphone(page: Page):
    def change_req(route: Route):
        resp = route.fetch()
        body = resp.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = phone_name
        body = json.dumps(body)
        route.fulfill(response=resp, body=body)

    page.route(re.compile('/shop/api/digital-mat'), change_req)
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone = page.get_by_role("button", name='Take a closer look ').locator('nth=0')
    iphone.click()
    title_popup = page.locator('#rf-digitalmat-overlay-label-0').locator('nth=0')
    expect(title_popup).to_contain_text(phone_name)
