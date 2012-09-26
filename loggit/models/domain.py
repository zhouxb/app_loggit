# -*- coding:utf8 -*-

import datetime
from collections import defaultdict
from mongoengine import *
from mongoengine.connection import get_connection, get_db, _dbs
from loggit.conf import settings

if settings.LOGGIT_PRODUCT:
    MONGODB_URI = 'mongodb://%s:%s@%s:%s/admin' % (settings.LOGGIT_MONGODB_USER, settings.LOGGIT_MONGODB_PASSWORD, settings.LOGGIT_MONGODB_HOST, settings.LOGGIT_MONGODB_PORT)
    connecting = connect('domain', alias='domain', host=MONGODB_URI)
    _dbs['domain'] = connecting['domain']
else:
    connect(settings.LOGGIT_TEST_DB, alias='domain', host=settings.LOGGIT_MONGODB_HOST, port=settings.LOGGIT_MONGODB_PORT)


class Minutely(Document):
    date = StringField()
    domain = StringField()
    count = IntField()
    namelist = StringField()
    isp = StringField()
    province = StringField()
    
    meta = {
            'db_alias':'domain',
            'allow_inheritance':False,
            }

