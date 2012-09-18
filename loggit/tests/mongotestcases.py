
import sys, os
import commands
from django.test import TransactionTestCase
from loggit.conf import settings


CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
FIXTURES_PATH = os.path.join(CURRENT_PATH, '../fixtures')
DB = settings.LOGGIT_TEST_DB

class TestCase(TransactionTestCase):
    def _fixture_setup(self):
        try:
            for testdata in self.fixtures:
                # FIXME
                collection = testdata.split('_')[1]
                create_cmd = 'mongoimport --db %s --collection %s --file %s/%s' % (DB, collection, FIXTURES_PATH, testdata)
                commands.getstatusoutput(create_cmd)
        except:
            pass

    def _fixture_teardown(self):
        drop_cmd = "mongo %s --eval 'db.dropDatabase()'" % DB
        commands.getstatusoutput(drop_cmd)

