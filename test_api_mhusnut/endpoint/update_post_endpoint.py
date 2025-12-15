import requests
import allure
from endpoint.base_endpoint import BaseEndpoint


class MethodPut(BaseEndpoint):

    def test_put_object(self, man_id, payload):
        with allure.step('Выполняем запрос'):
            self.response = requests.put(
                f'http://objapi.course.qa-practice.com/object/{man_id}',
                json=payload,
                headers=self.headers
            )
            self.json = self.response.json()
            return self.response

    def test_patch_object(self, man_id, payload):
        with allure.step('Выполняем запрос'):
            self.response = requests.patch(
                f'http://objapi.course.qa-practice.com/object/{man_id}',
                json=payload,
                headers=self.headers
            )
            self.json = self.response.json()
            return self.response
