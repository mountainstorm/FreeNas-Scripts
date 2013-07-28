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

# address list
HOST_LIST = [
	u'aa:bb:cc:dd:ee:ff'
]


#
# Processing
#

import socket
import struct


# wake all addresses
for addr in HOST_LIST:
	addr = addr.replace(u':', '')

	# add the magic header and repeats needed
	str_data = 'FFFFFFFFFFFF' + addr * 16
	
	data = ''
	for i in range(0, len(str_data), 2):
		data += struct.pack('B', int(str_data[i:i+2], 16))

	#i = 1
	#for c in data:
	#	print "%x" % ord(c),
	#	if not i % 6:
	#		print ""
	#	i += 1

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
	s.bind(('192.168.1.2', 7))
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	s.sendto(data, ('<broadcast>', 7))
