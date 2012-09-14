from mongoengine import *
from loggit.conf import settings

if settings.LOGGIT_PRODUCT:
    connect('newdomain', alias='newdomain', host=settings.LOGGIT_MONGODB_HOST, port=settings.LOGGIT_MONGODB_PORT)
else:
    connect(settings.LOGGIT_TEST_DB, alias='newdomain', host=settings.LOGGIT_MONGODB_HOST, port=settings.LOGGIT_MONGODB_PORT)

class Minutely(Document):
    date = StringField()
    domain = StringField()

    meta = {
            'db_alias':'newdomain',
            'allow_inheritance':False,
            }

