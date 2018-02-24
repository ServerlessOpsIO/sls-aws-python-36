'''<HANDLER DESCRIPTION>'''

import logging
import json
import os

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))
_logger = logging.getLogger(__name__)

def handler(event, context):
    '''Function entry'''

    resp = {}
    return json.dumps(resp)

