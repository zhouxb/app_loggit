# -*- coding:utf8 -*-

import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to

@render_to('loggit/domain/index.haml')
def index(request):
	today = datetime.date.today().strftime('%Y-%m-%d')
	starttime = request.REQUEST.get('starttime', None)
	endtime = request.REQUEST.get('endtime', None)

	starttime = starttime or today
	endtime = endtime or today

	return {'day':today, 'starttime':starttime, 'endtime':endtime}

@render_to('loggit/domain/namelist_index.haml')
def namelist(request):
	today = datetime.date.today().strftime('%Y-%m-%d')
	namelist = request.REQUEST.get('namelist', 'B')
	starttime = request.REQUEST.get('starttime', None)
	endtime = request.REQUEST.get('endtime', None)

	starttime = starttime or today
	endtime = endtime or today

	return {'day':today, 'starttime':starttime, 'endtime':endtime,'namelist':namelist}

@render_to('loggit/domain/namelistpercent_index.haml')
def namelistpercent(request):
	today = datetime.date.today().strftime('%Y-%m-%d')
	namelist = request.REQUEST.get('namelist', 'B')
	starttime = request.REQUEST.get('starttime', None)
	endtime = request.REQUEST.get('endtime', None)

	starttime = starttime or today
	endtime = endtime or today

	return {'day':today, 'starttime':starttime, 'endtime':endtime,'namelist':namelist}

@render_to('loggit/domain/alarm.haml')
def alarm(request):
	today = datetime.date.today().strftime('%Y-%m-%d')
	starttime = request.REQUEST.get('starttime', None)
	endtime = request.REQUEST.get('endtime', None)

	starttime = starttime or today
	endtime = endtime or today

	return {'day':today, 'starttime':starttime, 'endtime':endtime}

