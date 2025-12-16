import allure


class BaseEndpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None

    @allure.step('Check status code')
    def check_status_code(self):
        assert self.response.status_code == 200
