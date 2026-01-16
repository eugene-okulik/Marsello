from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_input_text(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    input_name = driver.find_element(By.CSS_SELECTOR, '#firstName')
    input_name.send_keys('Shrek')

    input_last_name = driver.find_element(By.CSS_SELECTOR, '#lastName')
    input_last_name.send_keys('Boloto')

    input_mail = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    input_mail.send_keys('name@example.com')

    gender = driver.find_element(By.CSS_SELECTOR, '.custom-control-label')
    gender.click()

    input_mobile = driver.find_element(By.CSS_SELECTOR, '#userNumber')
    input_mobile.send_keys('1111111111')

    input_birth_day = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput')
    input_birth_day.send_keys('20 Nov 2000')

    input_subjects = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    input_subjects.send_keys('Hindi')
    input_subjects.send_keys(Keys.ENTER)

    hobby = driver.find_element(By.CSS_SELECTOR, '[for="hobbies-checkbox-1"]')
    hobby.click()

    input_address = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
    input_address.send_keys('Grove Street')

    state_input = driver.find_element(By.CSS_SELECTOR, '#react-select-3-input')
    state_input.send_keys("NCR")
    state_input.send_keys(Keys.ENTER)

    city_input = driver.find_element(By.CSS_SELECTOR, '#react-select-4-input')
    city_input.send_keys("Delhi")
    city_input.send_keys(Keys.ENTER)

    submit_button = driver.find_element(By.CSS_SELECTOR, '#submit')
    submit_button.click()

    result = driver.find_element(By.CSS_SELECTOR, ".modal-dialog")
    result_text = result.text
    print(result_text)
