# -*- coding: utf-8 -*-
from datetime import datetime
import logging
from logging.config import dictConfig


LOG_PATH = (
    '/tmp/backtradercn-'
    f'{datetime.now().strftime("%Y%m%d-%H%M%S-%f")}.log'
)

logging_config = dict(
    version=1,
    formatters={
        'standard': {
            'format':
            '%(asctime)s %(name)s:%(lineno)d %(levelname)s: %(message)s',
            'default_msec_format': '%s.%03d',
            'converter': 'time.gmtime'
        }
    },
    handlers={
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': logging.DEBUG,
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'level': logging.DEBUG,
            'filename': LOG_PATH,
            'mode': 'a',
        }
    },
    root={
        'handlers': ['console', 'file'],
        'level': logging.DEBUG,
    },
)

dictConfig(logging_config)

# replace comma with period
# e.g.: 2010-09-06 22:38:15,292 => 2010-09-06 22:38:15.292
for h in logging.getLogger().handlers:
    h.formatter.default_msec_format = '%s.%03d'
