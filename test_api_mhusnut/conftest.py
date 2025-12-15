import pytest
import requests
from endpoint.create_post import MethodPost
from endpoint.update_post_endpoint import MethodPut
from endpoint.deleted_endpoint import MethodDelete


@pytest.fixture()
def create_post_endpoint():
    return MethodPost()


@pytest.fixture()
def update_post_endpoint():
    return MethodPut()


@pytest.fixture()
def delete_post_endpoint():
    return MethodDelete()


@pytest.fixture()
def man_id(create_post_endpoint):
    payload = {
        "name": "Марс",
        "data": {
            "years": 25,
            "place of residence": "РФ"
        }
    }
    headers = {'Content-Type': 'application/json'}

    create_post_endpoint.post_object(payload)
    yield create_post_endpoint.man_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{create_post_endpoint.man_id}',
                    headers=headers)
