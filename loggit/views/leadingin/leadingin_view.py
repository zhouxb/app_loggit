# -*- coding:utf8 -*-

import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to

@render_to('loggit/leadingin/index.haml')
def index(request):
	today = datetime.date.today().strftime('%Y-%m-%d')
	starttime = request.REQUEST.get('starttime', None)
	endtime = request.REQUEST.get('endtime', None)

	starttime = starttime or today
	endtime = endtime or today

	return {'day':today, 'starttime':starttime, 'endtime':endtime}