#!/bin/bash

env WORKFLOW=test_request.request_tests locust --host=http://10.162.36.231:8181 NikshayCaseListLocust
