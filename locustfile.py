from locust import HttpLocust

from task_sets.application import ApplicationTask


class ApplicationLocust(HttpLocust):
    task_set = ApplicationTask
    min_wait = 1000
    max_wait = 1000
