#!/usr/bin/env python
# coding: utf-8

# Copyright (c) 2013 Mountainstorm
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


#
# Settings
#

# Addresses to ping; when all are down we shutdown
HOST_LIST = [
	u'192.168.1.2',
	u'192.168.1.3'
]

# The time all hosts have to be down before we shutdown (in seconds)
# allow at LEAST 2 seconds per host
DOWNTIME_FOR_SHUTDOWN = 3600.0 # 1hr

# The time between tests; time between pings (in seconds)
DOWNTIME_TEST_TIMEOUT = 300.0 # 5 mins


#
# Processing
#

import os
import sys
import subprocess
from time import time, sleep


# prefil hosts with now
print(u'auto-shutdown.py: watching the following hosts:')
hosts = {}
for addr in HOST_LIST:
	print(u'auto-shutdown.py:  * %s' % addr)
	hosts[addr] = time()

# check if all addresses have been uncontactable for DOWNTIME_FOR_SHUTDOWN
devnull = open(os.devnull, 'w')
quit = False
while not quit:
	quit = True
	for addr in HOST_LIST:
		if subprocess.call(
				[u'/sbin/ping', u'-c', u'1', u'-t', u'1', addr], 
				stdout=devnull,
				stderr=devnull
			) == 0:
			hosts[addr] = time()

		if (time() - hosts[addr]) < DOWNTIME_FOR_SHUTDOWN:
			quit = False
	sleep(DOWNTIME_TEST_TIMEOUT)

# if all addresses are down; shutdown
if quit:
	print(u'auto-shutdown.py: watched hosts have done a runner, shutdown')
	subprocess.call([u'/bin/sync'])
	subprocess.call([u'/sbin/shutdown', u'-p', u'now'])
print(u'auto-shutdown.py: done')
