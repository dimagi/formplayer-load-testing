import os
import random
from locust import task

import settings
from task_sets.base import WebAppsTaskSet
from locust.log import console_logger


class CaseListTask(WebAppsTaskSet):

    @task
    def load_case_list(self):
        load_case_list(
            self.client,
            self.cookies,
            settings.RESTORE_AS,
            settings.CASE_LIST_SELECTIONS
        )


class MultiUserCaseListTask(WebAppsTaskSet):

    @task
    def load_case_list(self):
        load_case_list(
            self.client,
            self.cookies,
            str(random.randint(1, 500)),
            [1],
        )


class NikshayCaseListTask(WebAppsTaskSet):

    @task
    def load_case_list(self):
        workflow = os.environ.get('WORKFLOW')
        selections = settings.NIKSHAY_WORKFLOWS[workflow]
        load_case_list(self.client, self.cookies, settings.RESTORE_AS, selections)


def load_case_list(client, cookies, restore_as, selections):
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
            'restoreAs': restore_as,
            'username': settings.USERNAME,
        },
        'catch_response': True,
    }
    with client.post('/navigate_menu', **kwargs) as response:
        try:
            if response.json().get('status') == 'error':
                response.failure(response.json()['exception'])
        except ValueError:
            print 'Unable to decode JSON, odd.'
