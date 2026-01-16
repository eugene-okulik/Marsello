from selenium.webdriver.common.by import By


def test_input_text(driver):
    text = 'hesoyam'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_text = driver.find_element(By.CSS_SELECTOR, '#id_text_string')
    input_text.send_keys(text)
    input_text.submit()
    result_text = driver.find_element(By.CSS_SELECTOR, '#result-text')
    assert result_text.text == text
    print(result_text.text)
