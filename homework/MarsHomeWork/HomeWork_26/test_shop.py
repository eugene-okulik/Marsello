from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_task_one(driver):
    product = 'Customizable Desk'
    driver.get('http://testshop.qa-practice.com/')
    customizable_desk = driver.find_element(By.CSS_SELECTOR, '[alt="Customizable Desk"]')

    # Открываем в новой вкладке
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(customizable_desk).key_down(Keys.CONTROL).perform()

    # Переходим на новую вкладку
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Добавляем в корзину
    add_to_cart = driver.find_element(By.XPATH, '//a[@id="add_to_cart"]')
    add_to_cart.click()

    # Аппрув в попапе
    wait = WebDriverWait(driver, 7)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tr[class="js_product in_cart main_product"]')))
    continue_shopping = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-secondary"]')
    continue_shopping.click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'sup'), '1'))
    driver.close()

    # Переходим в корзину через 1 вкладку
    driver.switch_to.window(tabs[0])
    my_cart = driver.find_element(By.CSS_SELECTOR, '[class="fa fa-shopping-cart fa-stack"]')
    my_cart.click()

    # Переходим во вкладку корзины
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Проверяем
    my_buy = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9#attr=1,3"]')
    assert product in my_buy.text


def test_task_two(driver):
    product = 'Customizable Desk'
    driver.get('http://testshop.qa-practice.com/')

    # Находим локаторы
    customizable_desk = driver.find_element(By.CSS_SELECTOR, '[alt="Customizable Desk"]')
    add_to_cart = driver.find_element(By.CSS_SELECTOR, '[value="12"] + [role="button"]')

    # Наводимся на элемент и кликаем
    action = ActionChains(driver)
    action.move_to_element(customizable_desk)
    action.click(add_to_cart)
    action.perform()

    # Переходим в попап и проверяем
    wait = WebDriverWait(driver, 7)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'td > .product-name')))
    my_buy = driver.find_element(By.CSS_SELECTOR, 'td > .product-name')
    assert product in my_buy.text
