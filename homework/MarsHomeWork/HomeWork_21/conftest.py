import requests
import pytest
import allure


@pytest.fixture(scope='session')
def start_of_tests():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def start_full_tests():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def created_object_id():
    body = {
        "name": "Марс",
        "data": {
            "years": 25,
            "place of residence": "РФ"
        }
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    new_object_id = response.json()['id']
    assert response.status_code == 200, 'Status code is incorrect!'
    assert response.json()['name'] == 'Марс', 'Name is incorrect!'
    yield new_object_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}',
                    json=body, headers=headers
                    )
