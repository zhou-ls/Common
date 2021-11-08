# -*- coding: utf-8 -*-
from configparser import ConfigParser

conf = ConfigParser()
conf.read("enviro.ini")

host = conf.get("mysql", "host")
port = conf.getint("mysql", "port")

print(host, type(host))
print(port, type(port))
