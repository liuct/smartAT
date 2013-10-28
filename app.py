#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()  # monkey patch for gevent

from gevent.pywsgi import WSGIServer
from bottle import Bottle, static_file, redirect
import os

from smartapi.config import WEB_HOST, WEB_PORT  # import db configuration and arguments
from smartapi import api


# Below code is to fix known log issue because of mismatch on gevent and gunicorn
# http://stackoverflow.com/questions/9444405/gunicorn-and-websockets
def log_request(self):
    log = self.server.log
    if log:
        if hasattr(log, "info"):
            log.info(self.format_request() + '\n')
        else:
            log.write(self.format_request() + '\n')

import gevent
gevent.pywsgi.WSGIHandler.log_request = log_request
# end of fix

app = Bottle()

@app.get('/ping')
def ping():
    return 'pong'

@app.route("/smartserver/<filename:path>")
def assets(filename):
    return static_file(filename, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web'))


@app.route("/")
@app.route("/smartserver")
@app.route("/smartserver/")
def root():
    return redirect("/smartserver/index.html")


app.mount('/smartapi', api)


def main():
    port = WEB_PORT
    host = WEB_HOST
    print 'Smartserver Serving on %s:%d...' % (host, port)
    WSGIServer(("", port), app).serve_forever()

if __name__ == '__main__':
    main()
