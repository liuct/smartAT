#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from urlparse import urlparse

__all__ = [ "ZK_URI", "WEB_HOST", "WEB_PORT"]


ZK_URI = os.getenv("ZK_URI", "127.0.0.1:2181")
WEB_HOST = os.getenv("WEB_HOST", "")
WEB_PORT = int(os.getenv("WEB_PORT", "80"))