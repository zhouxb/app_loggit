# -*- coding:utf8 -*-

from annoying.decorators import render_to, ajax_request
from loggit.models.newdomain import Filter

@render_to('loggit/newdomain/filter/index.haml')
def index(request):
    day = request.GET.get('day', None)
    filters = Filter.objects()
    return {'filters':filters, 'day':day}

@ajax_request
def create(request):
    rule = request.GET.get('rule', None)
    if rule:
        Filter.objects.get_or_create(rule='*.%s' % rule)

    return {'result':'success'}

@ajax_request
def delete(request):
    id = request.GET.get('id', None)
    Filter.objects(id=id).delete()
    return {'result':'success'}

