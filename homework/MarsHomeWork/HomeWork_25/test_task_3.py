# Часть 1
# Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/select/single_select,
# выбирает какой-нибудь вариант из Choose language, кликает Submit и проверяет,
# что в окошке с результатом отображается тот вариант, который был выбран.
#
# Часть 2
# Напишите тест, который зайдет на страницу https://the-internet.herokuapp.com/dynamic_loading/2,
# нажмет Start, и проверит, что на странице появляется текст "Hello World!"


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_part_1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    drop_down = driver.find_element(By.CSS_SELECTOR, '[name="choose_language"]')
    drop_down.click()

    language = driver.find_element(By.CSS_SELECTOR, 'select[name="choose_language"]>option[value="1"]')
    language.click()
    language_name = language.text

    button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    button.click()

    result = driver.find_element(By.CSS_SELECTOR, '#result')
    final_text = result.text

    assert language_name in final_text


def test_part_2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    checked_text = 'Hello World!'
    wait = WebDriverWait(driver, 15)

    btn_start = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#start > button')))
    btn_start.click()

    wait.until(EC.text_to_be_present_in_element((By.ID, 'finish'), checked_text))

    finish = driver.find_element(By.CSS_SELECTOR, '#finish')
    fin_txt = finish.text
    assert checked_text == fin_txt
