#!/usr/bin/env python
from BaseHTTPServer import HTTPServer,  BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import sys
import os
from TakeReading import core

class HttpHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        try:
	    print "get message"
            mesg  =  self.path
            mesg = mesg.strip("/")
            mesg = mesg.split("&")
            myCore = core(mesg[0], mesg[2])
            myCore.process_package()
        except Exception, e:
	    print e
            pass #os.system("echo {0} >> /tmp/simba.log".format(e))
    
class MyHttpServer (ThreadingMixIn, HTTPServer):
    pass

def main():
    try:
        # depending on what we have in the Kannel file,  
        server = MyHttpServer(('localhost', 55555), HttpHandler)
        # os.system("echo {0} >> /tmp/simba.log".format(
        #       "Start Running Web Server, Waiting for Message."))
        server.serve_forever()
    except KeyboardInterrupt:
        print "Keyboard Interrupt - Closing Server"
        server.socket.close()
        sys.exit(0)    
    
if __name__  == '__main__':
    main()
