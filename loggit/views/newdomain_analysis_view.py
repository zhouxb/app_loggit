# -*- coding:utf8 -*-

import datetime
from django.core.cache import cache
from django.core.urlresolvers import reverse
from annoying.decorators import render_to
from loggit.models.newdomain import Minutely
from loggit.conf import settings

@render_to('loggit/newdomain/analysis/index.haml')
def index(request):
    day = request.GET.get('day', None)
    key = request.GET.get('key', None)

    timeout = settings.LOGGIT_TIMEOUT if day is None else 60

    if cache.get(day) is None:
        domains = list(Minutely.objects(date__startswith=day.replace('-', '')).values_list('domain', ))
        cache.set(day, domains, timeout)

    domains = cache.get(day)
    total = len(domains)

    n = 2
    if key:
        n = len(key.split('.')) + 1
    domains = Minutely.analysis(domains, n, key)

    return {'domains':domains, 'total':total, 'day':day, 'key':key}

