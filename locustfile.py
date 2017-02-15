from locust import HttpLocust

from task_sets.install import ApplicationTask
from task_sets.navigate_menu import CaseListTask
from task_sets.get_details import CaseDetailTask


class ApplicationLocust(HttpLocust):
    task_set = ApplicationTask
    min_wait = 1000
    max_wait = 1000


class CaseListLocust(HttpLocust):
    task_set = CaseListTask
    min_wait = 1000
    max_wait = 1000


class CaseDetailLocust(HttpLocust):
    task_set = CaseDetailTask
    min_wait = 1000
    max_wait = 1000
