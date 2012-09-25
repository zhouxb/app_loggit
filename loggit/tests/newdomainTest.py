# -*- coding:utf8 -*-

from mongotestcases import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
import simplejson

class NewDomainViewTest(TestCase):

    fixtures = ['newdomain_minutely_testdata.json', ]

    def setUp(self):
        self.c = Client()

    def test_index_on_success(self):
        response = self.c.get(
                reverse('loggit_api_newdomain_index'),
                {'day':20120827},
        )

        result = simplejson.loads(response.content)
        assert len(result['domains']) == 20

    #def test_show_have_two_on_success(self):
        #response = self.c.get(
                #reverse('loggit_api_newdomain_show'),
                #{'starttime':201208270000, 'endtime':201208272359},
        #)

        #result = simplejson.loads(response.content)
        #assert len(result['domains']) == 20

    #def test_show_have_only_starttime_on_success(self):
        #response = self.c.get(
                #reverse('loggit_api_newdomain_show'),
                #{'starttime':201208270000},
        #)

        #result = simplejson.loads(response.content)
        #assert len(result['domains']) == 20

    #def test_show_have_only_endtime_on_success(self):
        #response = self.c.get(
                #reverse('loggit_api_newdomain_show'),
                #{'endtime':201208272359},
        #)

        #result = simplejson.loads(response.content)
        #assert len(result['domains']) == 20

