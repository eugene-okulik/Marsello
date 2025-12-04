import requests


def post_object():
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
    return new_object_id


def put_object():
    new_object_id = post_object()
    body = {
        "name": "Марселло",
        "data": {
            "years": 255,
            "place of residence": "РФ"
        }
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect!'
    assert response.json()['data']['years'] == 255, 'Years is incorrect!'
    assert response.json()['name'] == 'Марселло', 'Name is incorrect!'
    clear(new_object_id)


def patch_object():
    new_object_id = post_object()
    body = {
        "data": {
            "years": 25
        }
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect!'
    assert response.json()['data']['years'] == 25, 'Years is incorrect!'
    clear(new_object_id)


def delete_object():
    new_object_id = post_object()
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}'
    )
    assert response.status_code == 200, 'Status code is incorrect!'


def clear(new_object_id):
    requests.delete(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}'
    )


post_object()
