'''<HANDLER DESCRIPTION>'''

import logging
import json
import os

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))  # type: ignore
_logger = logging.getLogger(__name__)


def handler(event, context):
    '''Function entry'''
    _logger.debug('Event received: {}'.format(json.dumps(event)))

    resp = {}
    _logger.debug('Response: {}'.format(json.dumps(resp)))
    return resp

