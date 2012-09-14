# -*- coding:utf8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to

@render_to('loggit/newdomain/index.haml')
def newdomain(request):
    return {}

