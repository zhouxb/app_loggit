from django.conf import settings
from appconf import AppConf

from mongoengine import *

class LoggitAppConf(AppConf):
    PRODUCT = True
    MONGODB_HOST = '111.1.32.93'
    MONGODB_PORT = 30000
    MONGODB_USER = 'root'
    MONGODB_PASSWORD = 'chinacache_is_really_hot'

    #PRODUCT = False
    #MONGODB_HOST = '192.168.10.93'
    #MONGODB_PORT = 27017
    ##TEST_DB = 'loggit'
    #TEST_DB = 'newdomain'

    TIMEOUT = 60*10

