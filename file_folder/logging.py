import logging
'''
NOTSET 0
DEBUG 10
INFO 20
WARNING 30
ERROR 40
CRITICAL 50
'''

logging.basicConfig(filename='newfile.log', format='%(asctime)s %(message)s', filemode='w')

# creating an object
logger = logging.getLogger()

# setting the threshold of the logger to debug
logger.setLevel(logging.WARNING)

logger.debug('Harmless debug message')
logger.info('Just an information')
logger.warning('Its a warning')
logger.error('Did you try to divide by zero')
logger.critical('Internet is down')


