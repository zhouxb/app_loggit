# -*- coding:utf8 -*-

import datetime
from collections import defaultdict
from mongoengine import *
from mongoengine.connection import get_connection, get_db, _dbs
from loggit.conf import settings

if settings.LOGGIT_PRODUCT:
    MONGODB_URI = 'mongodb://%s:%s@%s:%s/admin' % (settings.LOGGIT_MONGODB_USER, settings.LOGGIT_MONGODB_PASSWORD, settings.LOGGIT_MONGODB_HOST, settings.LOGGIT_MONGODB_PORT)
    connecting = connect('leadingin', alias='leadingin', host=MONGODB_URI)
    _dbs['leadingin'] = connecting['leadingin']
else:
    connect(settings.LOGGIT_TEST_DB, alias='leadingin', host=settings.LOGGIT_MONGODB_HOST, port=settings.LOGGIT_MONGODB_PORT)


class Minutely(Document):
    date = StringField()
    domain = StringField()
    isp = StringField()
    province = StringField()
    
    meta = {
            'db_alias':'leadingin',
            'allow_inheritance':False,
            }

