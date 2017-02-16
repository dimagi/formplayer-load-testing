from locust import task

import settings
from task_sets.base import WebAppsTaskSet


class CaseDetailTask(WebAppsTaskSet):

    @task
    def load_case_detail(self):
        self.client.post(
            '/get_details',
            cookies=self.cookies,
            headers={
                'Content-Type': 'application/json',
                'Host': settings.DJANGO_HOST,
            },
            json={
                'app_id': settings.APP_ID,
                'domain': settings.DOMAIN,
                'locale': "en",
                'offset': 0,
                'selections': settings.CASE_DETAIL_SELECTIONS,
                'oneQuestionPerScreen': False,
                'restoreAs': None,
                'username': settings.USERNAME,
            },
        )
