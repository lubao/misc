#!/usr/bin/env python
import SQLEng
import datetime
def main():
    patientInfo=SQLEng.SQLEng().exeSQL('SELECT `phone`, `freq`, `medication` FROM `care`.`reminder_reminder`')
    #print patientInfo
    if len(patientInfo) != 0:
        for info in patientInfo:
            # (phone,frequence,medication)
            curHour=datetime.datetime.now().hour
        if curHour==0 : curHour=24
        freq=int(info[1])
        if curHour % freq ==0:
            #SQLEng.SQLEng().exeSQL(SQLEng.SQLEng().getInsetSentBoxMsg(info[0], \
            #'''Please take your {0} medication'''.format(info[2])))
            print "Sending Reminder Message to "+info[0]

if __name__ == '__main__':
    main()
