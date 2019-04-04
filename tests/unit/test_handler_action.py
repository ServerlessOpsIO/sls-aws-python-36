'''Test health_event_publisher'''
# pylint: disable=protected-access
# pylint: disable=wrong-import-position
# pylint: disable=redefined-outer-name
import json
import os

#import boto3
#from moto import mock_sts
import pytest

import handlers.%%REPLACE_ME%% as h

EVENT_FILE = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'events',
        '%%REPLACE_ME%%.json'

)

@pytest.fixture()
def event(event_file=EVENT_FILE):
    '''Trigger event'''
    with open(event_file) as f:
        return json.load(f)


