# -*- coding:utf8 -*-

import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to, ajax_request

@render_to('loggit/timeline/index.haml')
def index(request):
    return {}

@ajax_request
def show(request):

    return {
    "timeline":
    {
        "type":"default",
        "date": [
            {
                "startDate":"2011,12,10",
                "endDate":"",
                "headline":"Headline Goes Here",
                "text":"<p>Body text goes here, some HTML is OK</p>",
                "asset": {
                    "media":"hello world",
                    "credit":"",
                    "caption":""
                }
            },
            {
                "startDate":"2011,12,11",
                "endDate":"",
                "headline":"Headline Goes Here",
                "text":"<p>Body text goes here, some HTML is OK</p>",
                "asset": {
                    "media":"hello world",
                    "credit":"",
                    "caption":""
                }
            },
            {
                "startDate":"2011,12,13",
                "endDate":"",
                "headline":"Headline Goes Here",
                "text":"<p>Body text goes here, some HTML is OK</p>",
                "asset": {
                    "media":"hello world",
                    "credit":"",
                    "caption":""
                }
            }
        ],
    }
}

