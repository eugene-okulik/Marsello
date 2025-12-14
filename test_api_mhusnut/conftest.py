import pytest
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
def post_id(create_post_endpoint):
    payload = {
        "name": "Марс",
        "data": {
            "years": 25,
            "place of residence": "РФ"
        }
    }
    create_post_endpoint.post_object(payload)
    yield create_post_endpoint.post_id
