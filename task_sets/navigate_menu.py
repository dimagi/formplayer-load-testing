import os
from locust import task

import settings
from task_sets.base import WebAppsTaskSet


class CaseListTask(WebAppsTaskSet):

    @task
    def load_case_list(self):
        load_case_list(self.client, self.cookies, settings.CASE_LIST_SELECTIONS)


class NikshayCaseListTask(CaseListTask):

    @task
    def load_case_list(self):
        workflow = os.environ.get('WORKFLOW')
        selections = settings.NIKSHAY_WORKFLOWS[workflow]
        load_case_list(self.client, self.cookies, selections)


def load_case_list(client, cookies, selections):
    client.post(
        '/navigate_menu',
        cookies=cookies,
        headers={
            'Content-Type': 'application/json',
        },
        json={
            'app_id': settings.CASE_LIST_APP_ID,
            'domain': settings.DOMAIN,
            'locale': "en",
            'offset': 0,
            'selections': selections,
            'oneQuestionPerScreen': False,
            'restoreAs': None,
            'username': settings.USERNAME,
        },
    )
