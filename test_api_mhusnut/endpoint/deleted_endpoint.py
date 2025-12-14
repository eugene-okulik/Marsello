import requests
from endpoint.base_endpoint import BaseEndpoint
import allure


class MethodDelete(BaseEndpoint):
    headers = None

    with allure.step('Создаем человечка'):
        def delete_object(self, post_id):
            self.response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}',
                                            headers=self.headers)

            return self.response
