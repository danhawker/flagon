from lib.bottle import Bottle, request, response
from datetime import datetime
from functools import wraps
import logging

logger = logging.getLogger('myapp')

# set up the logger
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('myapp.log')
formatter = logging.Formatter('%(msg)s')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log_to_logger(fn):
    '''
    Wrap a Bottle request so that a log line is emitted after it's handled.
    (This decorator can be extended to take the desired logger as a param.)
    '''
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        request_time = datetime.now()
        actual_response = fn(*args, **kwargs)
        # modify this to log exactly what you need:
        logger.info('%s %s %s %s %s' % (request.remote_addr,
                                        request_time,
                                        request.method,
                                        request.url,
                                        response.status))
        return actual_response
    return _log_to_logger

app = Bottle()
app.install(log_to_logger)

@app.route('/')
def home():
    return ['hello, world']

app.run(host='0.0.0.0', port='8080', quiet=True)
