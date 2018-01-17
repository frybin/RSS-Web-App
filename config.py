import os
from config_keys import *

SECRET_KEY=os.environ.get('SECRET_KEY') or secretkey
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+DB_USERNAME+':'+DB_PASSWORD+'@'+DB_HOST+'/'+DB
SQLALCHEMY_TRACK_MODIFICATIONS = False