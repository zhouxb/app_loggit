# -*- coding:utf8 -*-

import datetime
from mongotestcases import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from loggit.helpers.timeline_helper import day_on_num
import simplejson

class TimelineHelperTest(TestCase):

    def setUp(self):
        pass

    def test_day_on_num(self):
        start_day = datetime.date(2008, 8, 8)
        days = []
        for day in day_on_num(start_day, 30):
            days.append(day)

        assert days[0] == '20080808'
        assert days[-1] == '20080709'


class TimelineViewTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_show_on_success(self):
        response = self.c.get(
                reverse('loggit_timeline_show'),
        )
        result = simplejson.loads(response.content)
        print result
