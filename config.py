import os
from config_keys import *

def Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or secretkey