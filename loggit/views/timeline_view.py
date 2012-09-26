# -*- coding:utf8 -*-

import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to, ajax_request
from loggit.models.newdomain import Minutely
from loggit.helpers.timeline_helper import day_on_num
from django.core.cache import cache
from loggit.conf import settings

@render_to('loggit/timeline/index.haml')
def index(request):
    return {}

@ajax_request
def show(request):
    from mongoengine.queryset import Q
    import re

    timeline = {"type":"default"}
    date = []

    k = 'timeline'
    if cache.get(k) is None:
        for day in day_on_num(datetime.date.today(), 30):
            count = Minutely.by_day_count(day)

            year = day[:4]
            month = day[4:6]
            day = day[6:]

            starttime = '%s-%s-%s' % (year, month, day)
            endtime = starttime
            url = '%s?starttime=%s&endtime=%s' % (reverse('loggit_newdomain_show'), starttime, endtime)

            date.append({
                "startDate":"%s,%s,%s" % (year, month, day),
                "endDate":"",
                "headline":'newdomain %s' % str(count),
                "text":"<p>newdomain</p>",
                "asset": {
                    "media":"<a href=%s>%s</a>" % (url, str(count)),
                    "credit":"",
                    "caption":""
                }
            })
        cache.set(k, date, settings.LOGGIT_TIMEOUT)

    timeline['date'] = cache.get(k)

    return {'timeline':timeline}

