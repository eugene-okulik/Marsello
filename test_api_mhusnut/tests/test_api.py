import pytest
import allure

TEST_DATA = [
    {
        "name": "Марс",
        "data": {
            "years": 25,
            "place of residence": "РФ"
        }
    },
    {
        "name": "",
        "data": {
            "years": 25,
            "place of residence": "РФ"
        }
    }
]


@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Добавляем человечка')
@pytest.mark.critical
@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint, data):
    create_post_endpoint.post_object(payload=data)
    create_post_endpoint.check_status_code()


@allure.feature('Puts')
@allure.story('Manipulate puts')
@allure.title('Изменяем человечка')
@pytest.mark.medium
def test_put_object(update_post_endpoint, man_id):
    payload = {
        "name": "Марселло",
        "data": {
            "years": 255,
            "place of residence": "РФ"
        }
    }
    update_post_endpoint.test_put_object(man_id, payload)
    update_post_endpoint.check_status_code()


@allure.feature('Patchs')
@allure.story('Manipulate patch')
@allure.title('Изменяем человечку года')
def test_patch_object(update_post_endpoint, man_id):
    with allure.step('Вводим параметры человечка'):
        payload = {
            "data": {
                "years": 25
            }
        }

    update_post_endpoint.test_patch_object(man_id, payload)
    update_post_endpoint.check_status_code()


@allure.feature('Deletes')
@allure.story('Manipulate delete')
@allure.title('Удаляем человечка')
def test_delete_object(delete_post_endpoint, man_id):
    with allure.step('Выполняем запрос с конкретным id человечка'):
        delete_post_endpoint.delete_object(man_id)
        delete_post_endpoint.check_status_code()
