# -*- coding:utf8 -*-

from django import template

register = template.Library()

def ksplit(key):
    keys = key.split('.')
    keys.reverse()

    res_tmp = []
    buff = []

    for key in keys:
        buff.append(key)
        res_tmp.append(list(buff))

    result = []
    for res in res_tmp:
        res.reverse()
        result.append('.'.join(res))

    return result[1:]

register.filter('ksplit', ksplit)

