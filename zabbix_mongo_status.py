#!/usr/bin/python
#Script from https://github.com/srknc/zabbix_mongo_plugin

import sys
import urllib
import simplejson

f = urllib.urlopen("http://127.0.0.1:28017/_status" )
data=simplejson.loads(f.read())

condition=data[sys.argv[1]][sys.argv[2]]
if len(sys.argv) == 5:
        print condition [sys.argv[3]] [sys.argv[4]]
elif len(sys.argv) == 4:
        print condition [sys.argv[3]]
else:
        print condition

