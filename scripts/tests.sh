#!/bin/bash

env WORKFLOW=tests locust --host=http://10.162.36.231:8181 NikshayCaseListLocust
