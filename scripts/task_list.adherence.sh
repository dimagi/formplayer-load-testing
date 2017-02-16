#!/bin/bash

env WORKFLOW=task_list.adherence locust --host=http://10.162.36.231:8181 NikshayCaseListLocust
