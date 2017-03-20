import os
from locust import task

import settings
from task_sets.base import WebAppsTaskSet
from locust.log import console_logger


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
    kwargs = {
        'cookies': cookies,
        'headers': {
            'Content-Type': 'application/json',
            'Host': settings.DJANGO_HOST,
        },
        'json': {
            'app_id': settings.APP_ID,
            'domain': settings.DOMAIN,
            'locale': "en",
            'offset': 0,
            'selections': selections,
            'oneQuestionPerScreen': False,
            'restoreAs': settings.RESTORE_AS,
            'username': settings.USERNAME,
        },
        'catch_response': True,
    }
    with client.post('/navigate_menu', **kwargs) as response:
        if response.json().get('status') == 'error':
            response.failure(response.json()['exception'])
