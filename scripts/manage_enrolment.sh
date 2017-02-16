#!/bin/bash

env WORKFLOW=manage_enrolment locust --host=http://10.162.36.231:8181 NikshayCaseListLocust
