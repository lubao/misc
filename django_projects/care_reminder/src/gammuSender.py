'''
Created on Jan 18, 2010

@author: Paul
'''
from SQLEng import SQLEng

class pduSender(object):
    '''
    classdocs
    This class is designed for Gammu-smsd
    Inserting a record into MySQL
    Gammu-smsd will send the record
    Using command line will cause smsd stop for a while
    '''
    def getMesg(self,byteArray):
        mesg=""
        for byte in byteArray:
            if byte < 16 :
                val=hex(byte)
                if val=="0x0" : val="00"
                else :
                    val=val.lstrip("0x")
                    val="{0}{1}".format('0',val)
            else :
                val=hex(byte)
                val=val.lstrip("0x")
            mesg+=val
        return mesg
    def send(self,to,byteArray):
        sEng=SQLEng()
        sEng.exeSQL(sEng.getInsetSentBox(to, self.getMesg(byteArray)))
    def __init__(self):
        '''
        Constructor
        '''
        pass
        