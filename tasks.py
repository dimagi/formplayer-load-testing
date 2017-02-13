import os
from collections import namedtuple
from jinja2 import Environment, FileSystemLoader

import settings
from invoke import task

Phase = namedtuple('Phase', 'duration, arrival_rate')

# Test types
APPLICATION_TYPE = 'application'

TEST_TYPES = [
    APPLICATION_TYPE
]


@task
def tsung_build(ctx, test_type, user_rate=10, duration=60):
    if test_type not in TEST_TYPES:
        print 'Unknown test type {}. Available test types: {}'.format(test_type, ', '.join(TEST_TYPES))
        return
    user_rate = int(user_rate)
    duration = int(user_rate)
    phases = [Phase(duration=duration, arrival_rate=user_rate)]

    context = tsung_template_context(phases)

    new_filename = os.path.join(settings.BUILD_DIR, '{}.xml'.format(test_type))
    filename = get_template_filename(test_type)

    with open(new_filename, 'w') as f:
        f.write(_render_template(filename, context))
        print("Built config: {}".format(new_filename))


def tsung_template_context(phases):
    return {
        'dtd_path': settings.TSUNG_DTD_PATH,
        'phases': phases,
        'host': settings.FORMPLAYER_HOST,
        'port': settings.FORMPLAYER_PORT,
        'domain': settings.DOMAIN,
    }


def get_template_filename(test_type):
    return '{}.xml.j2'.format(test_type)


def _render_template(filename, context):
    env = Environment(loader=FileSystemLoader([settings.TEMPLATE_DIR]))
    template = env.get_template(filename)
    return template.render(**context)
