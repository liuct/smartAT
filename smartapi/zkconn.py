#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
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
		if data is not None and len(data) > 0:
		    pi_list.append(json.loads(data[0]))
	zk.stop()
	return pi_list
