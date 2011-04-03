#!/usr/bin/env python
'''
Created on 2010/1/14

@author: Administrator
'''
from socket import *
import sys

def runOnReceive():
    for arg in sys.argv:
        print arg

if __name__ == '__main__':
    #runOnReceive()
    host="localhost"
    port=20000
    buf=4
    addr=(host,port)
    UDPSock=socket(AF_INET,SOCK_DGRAM)
    print "send {0} to server".format(sys.argv[1])
    UDPSock.sendto(sys.argv[1],addr)
    UDPSock.close()
    exit()
