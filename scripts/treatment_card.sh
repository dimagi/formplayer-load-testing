#!/bin/bash

env WORKFLOW=treatment_card locust --host=http://10.162.36.231:8181 NikshayCaseListLocust
