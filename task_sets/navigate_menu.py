from locust import task

import settings
from task_sets.base import WebAppsTaskSet

class CaseListTask(WebAppsTaskSet):

    @task
    def load_case_list(self):
        self.client.post(
            '/navigate_menu',
            cookies=self.cookies,
            headers={
                'Content-Type': 'application/json',
            },
            json={
                'app_id': settings.CASE_LIST_APP_ID,
                'domain': settings.DOMAIN,
                'locale': "en",
                'offset': 0,
                'selections': settings.CASE_LIST_SELECTIONS,
                'oneQuestionPerScreen': False,
                'restoreAs': None,
                'username': settings.USERNAME,
            },
        )
