from django.conf import settings
from appconf import AppConf

from mongoengine import *

class LoggitAppConf(AppConf):
    PRODUCT = True
    MONGODB_HOST = '111.1.32.93'
    MONGODB_PORT = 30000

    #PRODUCT = False
    #MONGODB_HOST = '127.0.0.1'
    #MONGODB_PORT = 27017
    TEST_DB = 'loggit'

    TIMEOUT = 60*10

