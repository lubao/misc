#!/usr/bin/env python
from TakeReading import core
fn = [l.strip().split()[7].split('55555/')[1].rstrip('\':\"') for l in open('url','r').readlines()]
for mesg in fn:
	try:
		mesg = mesg.split("&")
		if len(mesg[2]) > 100:
			#print mesg
			myCore = core(mesg[0], mesg[2])
			myCore.process_package()
	except Exception, e:
		print e
		pass #os.system("echo {0} >> /tmp/simba.log".format(e))
