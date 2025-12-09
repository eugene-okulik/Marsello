import requests
import pytest
import allure


@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Добавляем человечка')
@pytest.mark.critical
@pytest.mark.parametrize('name', ['@Mapc123', '', '123123'])
def test_post_object(start_of_tests, name, start_full_tests):
    with allure.step('Вводим параметры человечка'):
        body = {
            "name": name,
            "data": {
                "years": 25,
                "place of residence": "РФ"
            }
        }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Выполняем запрос'):
        response = requests.post(
            'http://objapi.course.qa-practice.com/object',
            json=body,
            headers=headers
        )
    id = response.json()['id']

    with allure.step('Проверяем статус ответа'):
        assert response.status_code == 200, 'Status code is incorrect!'

    with allure.step('Проверяем корректность поля name'):
        assert response.json()['name'] == name, 'Name is incorrect!'

    requests.delete(
        f'http://objapi.course.qa-practice.com/object/{id}'
    )


@allure.feature('Puts')
@allure.story('Manipulate puts')
@allure.title('Изменяем человечка')
@pytest.mark.medium
def test_put_object(created_object_id, start_full_tests):
    with allure.step('Вводим параметры человечка'):
        body = {
            "name": "Марселло",
            "data": {
                "years": 255,
                "place of residence": "РФ"
            }
        }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Выполняем запрос'):
        response = requests.put(
            f'http://objapi.course.qa-practice.com/object/{created_object_id}',
            json=body,
            headers=headers
        )

    with allure.step('Проверяем статус ответа'):
        assert response.status_code == 200, 'Status code is incorrect!'

    with allure.step('Проверяем корректность заполнения поля data'):
        assert response.json()['data']['years'] == 255, 'Years is incorrect!'

    with allure.step('Проверяем корректность заполнения поля name'):
        assert response.json()['name'] == 'Марселло', 'Name is incorrect!'


@allure.feature('Patchs')
@allure.story('Manipulate patch')
@allure.title('Изменяем человечку года')
def test_patch_object(created_object_id, start_full_tests):
    with allure.step('Вводим параметры человечка'):
        body = {
            "data": {
                "years": 25
            }
        }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Выполняем запрос'):
        response = requests.patch(
            f'http://objapi.course.qa-practice.com/object/{created_object_id}',
            json=body,
            headers=headers
        )

    with allure.step('Проверяем статус ответа'):
        assert response.status_code == 200, 'Status code is incorrect!'

    with allure.step('Проверяем корректность заполнения поля data'):
        assert response.json()['data']['years'] == 25, 'Years is incorrect!'


@allure.feature('Deletes')
@allure.story('Manipulate delete')
@allure.title('Удаляем человечка')
def test_delete_object(created_object_id, start_full_tests):
    with allure.step('Выполняем запрос с конкретным id человечка'):
        response = requests.delete(
            f'http://objapi.course.qa-practice.com/object/{created_object_id}'
        )

    with allure.step('Проверяем статус ответа'):
        assert response.status_code == 200, 'Status code is incorrect!'
