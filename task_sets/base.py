from locust import TaskSet

import settings


class WebAppsTaskSet(TaskSet):

    def on_start(self):
        # Get csrf token from django
        login_response = self.client.get('{}/a/{}/login/'.format(
            settings.DJANGO_HOST,
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
            '{}/a/{}/login/'.format(settings.DJANGO_HOST, settings.DOMAIN),
            cookies=login_response.cookies,
            headers=headers,
            data=data,
        )
        self.cookies = auth_response.cookies
