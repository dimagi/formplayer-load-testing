from locust import task

import settings
from task_sets.base import WebAppsTaskSet


class ApplicationTask(WebAppsTaskSet):

    @task
    def install(self):
        self.client.post(
            '/install',
            cookies=self.cookies,
            headers={
                'Content-Type': 'application/json',
                'Host': settings.DJANGO_HOST,
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
