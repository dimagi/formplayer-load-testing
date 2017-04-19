#!/bin/bash

env WORKFLOW=home_visits locust --host=http://10.162.36.231:8181 NikshayCaseListLocust
