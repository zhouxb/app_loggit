# -*- coding:utf8 -*-

import datetime
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to
from loggit.models.newdomain import Minutely, Filter
from loggit.conf import settings

def create(request):
    #print dir(request)
    #print request.path
    #print request.get_full_path()
    #print request

    #rule = request.POST.get('rule', None)
    #if rule:
        #filter = Filter(rule=rule)
        #filter.save()

    return {}

