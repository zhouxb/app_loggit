# -*- coding:utf8 -*-

import datetime
import re
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to
from loggit.models.newdomain import Minutely, Filter
from loggit.conf import settings
from mongoengine.queryset import Q

@render_to('loggit/newdomain/analysis/index.haml')
def index(request):
    day = request.GET.get('day', None)
    key = request.GET.get('key', None)

    domains = Minutely.by_day(starttime=day, endtime=day)
    total = len(domains)

    n = len(key.split('.')) + 1 if key else 2
    domains = Minutely.analysis(domains, n, key)

    return {'domains':domains, 'total':total, 'day':day, 'key':key}

