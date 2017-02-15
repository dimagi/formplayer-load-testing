import settings
from locust import HttpLocust, TaskSet, task


class ApplicationTask(TaskSet):

    def on_start(self):
        # Get csrf token from django
        login_response = self.client.get('http://localhost:8000/a/aspace/login/')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': login_response.cookies.get('csrftoken'),
        }
        data = {
            'auth-username': settings.USERNAME,
            'auth-password': settings.PASSWORD,
            'cloud_care_login_view-current_step': 'auth'
        }

        auth_response = self.client.post(
            '{}/a/{}/login/'.format(settings.DJANGO_HOST, settings.DOMAIN),
            cookies=login_response.cookies,
            headers=headers,
            data=data,
        )
        self.cookies = auth_response.cookies

    @task
    def install(self):
        self.client.post(
            '/install',
            cookies=self.cookies,
            headers={
                'Content-Type': 'application/json',
            },
            json={
                'app_id': settings.APP_ID,
                'domain': settings.DOMAIN,
                'locale': "en",
                'offset': None,
                'oneQuestionPerScreen': False,
                'restoreAs': None,
                'username': settings.USERNAME,
            },
        )


class ApplicationLocust(HttpLocust):
    task_set = ApplicationTask
    min_wait = 1000
    max_wait = 1000
