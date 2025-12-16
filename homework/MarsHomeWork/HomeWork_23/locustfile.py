from locust import task, HttpUser


class Users(HttpUser):
    new_object_id = None
    headers = {'Content-Type': 'application/json'}
    host = 'http://objapi.course.qa-practice.com'

    def on_start(self):
        body = {
            "name": "Марс",
            "data": {
                "years": 25,
                "place of residence": "РФ"
            }
        }

        response = self.client.post(
            '/object',
            json=body,
            headers=self.headers
        )
        self.new_object_id = response.json()['id']

    @task(4)
    def get_all_object(self):
        self.client.get(
            '/object',
            headers=self.headers
        )

    @task(1)
    def get_one_object(self):
        self.client.get(
            f'/object/{self.new_object_id}',
            headers=self.headers
        )
