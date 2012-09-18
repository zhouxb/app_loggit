from mongoengine import *
from mongoengine.connection import get_connection, get_db, _dbs
from loggit.conf import settings

if settings.LOGGIT_PRODUCT:
    MONGODB_URI = 'mongodb://%s:%s@%s:%s/admin' % (settings.LOGGIT_MONGODB_USER, settings.LOGGIT_MONGODB_PASSWORD, settings.LOGGIT_MONGODB_HOST, settings.LOGGIT_MONGODB_PORT)
    connecting = connect('newdomain', alias='newdomain', host=MONGODB_URI)
    _dbs['newdomain'] = connecting['newdomain']
else:
    connect(settings.LOGGIT_TEST_DB, alias='newdomain', host=settings.LOGGIT_MONGODB_HOST, port=settings.LOGGIT_MONGODB_PORT)

class Minutely(Document):
    date = StringField()
    domain = StringField()

    meta = {
            'db_alias':'newdomain',
            'allow_inheritance':False,
            }

