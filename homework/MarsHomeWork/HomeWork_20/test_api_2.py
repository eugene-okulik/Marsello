import requests
import pytest


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


@pytest.mark.critical
@pytest.mark.parametrize('name', ['@Mapc123', '', '123123'])
def test_post_object(start_of_tests, name, start_full_tests):
    body = {
        "name": name,
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
    id = response.json()['id']
    assert response.status_code == 200, 'Status code is incorrect!'
    assert response.json()['name'] == name, 'Name is incorrect!'
    requests.delete(
        f'http://objapi.course.qa-practice.com/object/{id}'
    )


@pytest.mark.medium
def test_put_object(created_object_id, start_full_tests):
    body = {
        "name": "Марселло",
        "data": {
            "years": 255,
            "place of residence": "РФ"
        }
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{created_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect!'
    assert response.json()['data']['years'] == 255, 'Years is incorrect!'
    assert response.json()['name'] == 'Марселло', 'Name is incorrect!'


def test_patch_object(created_object_id, start_full_tests):
    body = {
        "data": {
            "years": 25
        }
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{created_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect!'
    assert response.json()['data']['years'] == 25, 'Years is incorrect!'


def test_delete_object(created_object_id, start_full_tests):
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{created_object_id}'
    )
    assert response.status_code == 200, 'Status code is incorrect!'
