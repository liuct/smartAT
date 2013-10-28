#!/usr/bin/env python

from gevent import monkey
monkey.patch_all()

from bottle import request, response, Bottle, HTTPResponse
from zkconn import *

api = Bottle()

@api.route('/devices', method='GET')
def doGetDeviceList():
    """
    """
    rdata = get_devices_list()
    return {"results": rdata}

