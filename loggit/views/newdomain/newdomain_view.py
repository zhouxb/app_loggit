# -*- coding:utf8 -*-

import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to

@render_to('loggit/newdomain/index.haml')
def index(request):
    today = datetime.date.today().strftime('%Y-%m-%d')
    starttime = request.GET.get('starttime', None)
    endtime = request.GET.get('endtime', None)

    starttime = starttime or today
    endtime = endtime or today

    return {'day':today, 'starttime':starttime, 'endtime':endtime}

@render_to('loggit/newdomain/show.haml')
def show(request):
    today = datetime.date.today().strftime('%Y-%m-%d')
    starttime = request.GET.get('starttime', None)
    endtime = request.GET.get('endtime', None)

    return {'day':today, 'starttime':starttime, 'endtime':endtime}

