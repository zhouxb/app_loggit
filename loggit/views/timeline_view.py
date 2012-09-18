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

    timeline = {"type":"default"}
    date = []

    k = 'timeline'
    if cache.get(k) is None:
        for day in day_on_num(datetime.date.today(), 30):
            count = Minutely.objects(date__startswith=day).count()

            date.append({
                "startDate":"%s,%s,%s" % (day[:4], day[4:6], day[6:]),
                "endDate":"",
                "headline":'newdomain %s' % str(count),
                "text":"<p>newdomain</p>",
                "asset": {
                    "media":"<h3>%s</h3>" % str(count),
                    "credit":"",
                    "caption":""
                }
            })
        cache.set(k, date, settings.LOGGIT_TIMEOUT)

    timeline['date'] = cache.get(k)

    return {'timeline':timeline}

