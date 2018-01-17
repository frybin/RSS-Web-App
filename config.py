import os
from config_keys import *

SECRET_KEY=os.environ.get('SECRET_KEY') or secretkey