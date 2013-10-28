#!/usr/bin/env python

from gevent import monkey
monkey.patch_all()

from bottle import request, response, Bottle, HTTPResponse
from zkconn import *

api = Bottle()

@api.get('/devices')
def doGetDeviceList():
    """
    """
    rdata = get_devices_list()
    return {"results": rdata}

@api.post('/<ip>/<sn>/start')
def doStartJob():
	pass

@api.post('/<ip>/<sn>/stop')
def doStopJob():
	pass

@api.post('/<ip>/<sn>/<jid>/stream')
def doJobStream():
	pass

@api.delete('/<ip>/<jid>')
def doDeleteJob():
	pass

@api.get('/<ip>/jobs')
def doGetJobs():
	pass

