from locust import TaskSet
from time import sleep
from locust.log import console_logger

import settings


class WebAppsTaskSet(TaskSet):

    def on_start(self):
        # You will want to get a session id if doing a lot of testing
        if hasattr(settings, 'SESSION_ID'):
            self.cookies = {
                'sessionid': settings.SESSION_ID,
            }
            return

        login_response = self.client.get('{}/a/{}/login/'.format(
            settings.DJANGO_URI,
            settings.DOMAIN
        ))

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
            '{}/a/{}/login/'.format(settings.DJANGO_URI, settings.DOMAIN),
            cookies=login_response.cookies,
            headers=headers,
            data=data,
        )
        self.cookies = auth_response.cookies

        # Sync that database
        sync_db(self.client, self.cookies)


def sync_db(client, cookies):
    response = _sync_db(client, cookies)
    console_logger.info('Sync response code: {}'.format(response.status_code))
    if response.json().get('status') == 'error':
        raise Exception(response.json()['exception'])

    while response.status_code == 202:
        sleep(response.json()['retryAfter'])
        response = _sync_db(client, cookies)
        console_logger.info('Sync response code: {}'.format(response.status_code))
        if response.json().get('status') == 'error':
            raise Exception(response.json()['exception'])


def _sync_db(client, cookies):
    return client.post(
        '/sync-db',
        cookies=cookies,
        headers={
            'Content-Type': 'application/json',
            'Host': settings.DJANGO_HOST,
        },
        json={
            'domain': settings.DOMAIN,
            'restoreAs': settings.RESTORE_AS,
            'username': settings.USERNAME,
            'preserveCache': True,
        }
    )
