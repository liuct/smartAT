#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from config import ZK_URI, PI_PATH
from kazoo.client import KazooClient

__all__ = ["get_devices_list"]

#PI_PATH = "/pi"
JOIN = os.path.join

def get_devices_list():
	pi_list = []
	zk = KazooClient(hosts=ZK_URI)
	zk.start()
	subs = zk.get_children(PI_PATH)
	for sub in subs:
		data = zk.get(JOIN(PI_PATH, sub))
		if data is not None:
			#values = data[0].split(':')
			#if len(values) > 1:
			#	pi_list.append({'ip': values[0], 'deviceid': values[1],'product': values[2], 'build': values[3] })
			#else:
			#	pi_list.append({'ip': values[0], 'deviceid': '','product': '', 'build': ''})
			pi_list.append(data)
	zk.stop()
	return pi_list
