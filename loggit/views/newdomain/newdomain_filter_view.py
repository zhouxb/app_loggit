# -*- coding:utf8 -*-

from annoying.decorators import render_to, ajax_request
from loggit.models.newdomain import Filter
from loggit.helpers.filter_helper import rule_update

@render_to('loggit/newdomain/filter/index.haml')
def index(request):
    day = request.GET.get('day', None)
    filters = Filter.objects()
    return {'filters':filters, 'day':day}

@ajax_request
def create(request):
    rule = request.GET.get('rule', None)
    if rule:
        rule = '*.%s' % rule
        old_rules = Filter.objects.values_list('rule')
        add_rules, del_rules = rule_update(old_rules, rule)

        for r in add_rules:
            Filter.objects.get_or_create(rule=r)
        for r in del_rules:
            Filter.objects(rule=r).delete()

    return {'result':'success'}

@ajax_request
def delete(request):
    id = request.GET.get('id', None)
    Filter.objects(id=id).delete()
    return {'result':'success'}

