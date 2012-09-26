# -*- coding:utf8 -*-

import datetime
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import ajax_request
from loggit.models.newdomain import Minutely, Filter
from loggit.conf import settings

@ajax_request
def create(request):
    rule = request.GET.get('rule', None)
    if rule:
        Filter.objects.get_or_create(rule='*.%s' % rule)

    return {'result':'success'}

