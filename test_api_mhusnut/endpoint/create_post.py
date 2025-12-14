import requests
from endpoint.base_endpoint import BaseEndpoint
import allure


class MethodPost(BaseEndpoint):
    def post_object(self, payload, headers=None):
        with allure.step('Создаем человечка'):
            self.response = requests.post(f'{self.url}', json=payload, headers=self.headers)

            self.json = self.response.json()
            self.post_id = self.json['id']
            return self.response
