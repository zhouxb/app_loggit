# -*- coding:utf8 -*-

import re
import datetime
from collections import defaultdict
from django.core.cache import cache
from mongoengine import *
from mongoengine.connection import get_connection, get_db, _dbs
from mongoengine.queryset import Q
from loggit.conf import settings

if settings.LOGGIT_PRODUCT:
    MONGODB_URI = 'mongodb://%s:%s@%s:%s/admin' % (settings.LOGGIT_MONGODB_USER, settings.LOGGIT_MONGODB_PASSWORD, settings.LOGGIT_MONGODB_HOST, settings.LOGGIT_MONGODB_PORT)
    connecting = connect('newdomain', alias='newdomain', host=MONGODB_URI)
    _dbs['newdomain'] = connecting['newdomain']
else:
    connect(settings.LOGGIT_TEST_DB, alias='newdomain', host=settings.LOGGIT_MONGODB_HOST, port=settings.LOGGIT_MONGODB_PORT)

class Minutely(Document):
    date = StringField()
    domain = StringField()

    meta = {
            'db_alias':'newdomain',
            'allow_inheritance':False,
            }

    @classmethod
    def by_day_count(cls, day):
        rules = list(Filter.objects.values_list('rule'))
        if rules:
            rules = '|'.join(map(lambda x:'.%s' % x, rules))
            count = Minutely.objects(Q(date__startswith=day) & Q(domain__not__regex=rules)).count()
        else:
            count = Minutely.objects(Q(date__startswith=day)).count()

        return count

    @classmethod
    def by_day(cls, starttime, endtime):
        starttime = starttime.replace('-', '')
        endtime = endtime.replace('-', '')

        if starttime == endtime:
            cache_key = 'newdomain%s' % starttime
            if cache.get(cache_key) is None:
                domains = list(cls.objects(date__startswith=starttime).values_list('domain', ))
                cache.set(cache_key, domains, 60)
        else:
            cache_key = 'newdomain%s_%s' % (starttime, endtime)
            if cache.get(cache_key) is None:
                if starttime is None:
                    domains = list(cls.objects(date__lte=endtime).values_list('domain', ))
                elif endtime is None:
                    domains = list(cls.objects(date__gte=starttime).values_list('domain', ))
                else:
                    domains = list(cls.objects(date__gte=starttime, date__lte=endtime).values_list('domain', ))
                cache.set(cache_key, domains, settings.LOGGIT_TIMEOUT)

        domains = cache.get(cache_key)

        rules = list(Filter.objects.values_list('rule'))
        if rules:
            rules = '|'.join(map(lambda x:'.%s' % x, rules))
            domains = filter(lambda x:not re.match(rules, x), domains)

        return domains

    @classmethod
    def analysis(cls, domains, n=2, key=None):
        if key:
            domains = filter(lambda x: x.endswith(key), domains)

        unordered_info = group_domain(n)(domains).items()
        ordered_info = sorted(map(lambda x: (len(x[1]), x[0]), unordered_info), reverse=True)

        domains_collection = []
        for count, domain in ordered_info:
            domains_collection.append({'domain':domain, 'count':count})

        return domains_collection

def get_level(n):
    def inner(domain):
        parts = domain.split(".")
        return ".".join(parts[-n:])
    return inner

def groupby(items, func):
    table = defaultdict(list)
    for item in items:
        key = func(item)
        table[key].append(item)
    return table

def group_domain(n):
    def inner(domains):
        return groupby(domains, get_level(n))
    return inner

class Filter(Document):
    date = DateTimeField(default=datetime.datetime.now)
    rule = StringField()

    meta = {
            'db_alias':'newdomain',
            'allow_inheritance':False,
    }

