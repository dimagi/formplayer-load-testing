#!/bin/bash

env WORKFLOW=view_patients locust --host=http://10.162.36.231:8181 NikshayCaseListLocust
