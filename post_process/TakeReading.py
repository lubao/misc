#!/usr/bin/env python
import array
import MySQLdb
import os 
class core():

    def __init__(self, phone, mesg):
        self.phone = phone
        self.package_array = self.get_pkg_byte_array(mesg)

    def get_pkg_byte_array(self,text):
        # There are two different case in percentage encoding
        # r=> %72 or 'r'
        # we have to take care of both
        pkg=array.array('B')# UNSIGNED CHARACTER => 1 BYTE
        pos=0
        while pos < len(text):
            if text[pos] == '%' :
                pkg.append(int(text[pos+1:pos+3], 16))
                pos+=3
            elif text[pos]=='+':
                # In case,  the byte is 0x2b,  it must be encode into %2b
                # Thus,  '+',  which code is 0x2b,  does not mean 0x2b
                # for some reason,  it used to replace the value of  0x20
                pkg.append(0x20)
                pos+=1
            else :
                pkg.append(ord(text[pos]))
                pos+=1
        return pkg
 
    def process_package(self, RANGE_OF_FIELD=10, NUM_OF_FIELD=6, CUR_BIT_POS=0):
        # might need to change # of fields here based on # of readings 
        # and the Range of Field (if getting values above 256 then 
        # need to change range of field to 10 can be 8 
        # if range is less than 256)
        # need to change in Arduino as well if we change the values here		
		print 'Process Package'
		RANGE_MONTH = 4
		RANGE_DAY = 5 
		RANGE_HOUR = 5
		RANGE_MIN = 6
		RANGE_OF_DATE = 20
		tmp = NUM_OF_FIELD*RANGE_OF_FIELD + RANGE_OF_DATE
		if tmp%8:
			tmp = tmp/8+1
		else:
			tmp /= 8
		NUM_OF_REC=133/tmp
		print 'NUM OF REC '+str(NUM_OF_REC)
		while NUM_OF_REC >0 :
			NUM_OF_REC -= 1
			data = []
			for i in range(NUM_OF_FIELD):
				val = self.get_integer_value(
							   self.package_array, CUR_BIT_POS, RANGE_OF_FIELD)
				val = float (5 * val)
				x = float(float(val/1023)/0.180238)
				#print x
				data.append(("%0.2f" % x))
				#data.append(x)
				CUR_BIT_POS+=RANGE_OF_FIELD
			print 'get date time'
			mon = (self.get_integer_value(self.package_array, CUR_BIT_POS, RANGE_MONTH))
			print 'get date time'
			CUR_BIT_POS += RANGE_MONTH
			day = (self.get_integer_value(self.package_array, CUR_BIT_POS, RANGE_DAY))
			print 'get date time'
			CUR_BIT_POS += RANGE_DAY
			hur = (self.get_integer_value(self.package_array, CUR_BIT_POS, RANGE_HOUR))
			print 'get date time'
			CUR_BIT_POS += RANGE_HOUR
			sec = (self.get_integer_value(self.package_array, CUR_BIT_POS, RANGE_MIN))
			print 'get date time'
			CUR_BIT_POS += RANGE_MIN
			data.append("2011-{0}-{1} {2}:{3}:00".
										format(mon,  day,  hur,  sec))
			sql=self.get_insert_reading_sql(self.phone, data)
			if sql != 'no_act':
				#print "Insert Reading to Database: " + sql
			#with open("/tmp/simba.log","a") as fh:
			#    fh.write(sql+"\n")
				self.execute_sql(sql)
			else:
				print 'not ethopia'

    def execute_sql(self, SQL):
		print SQL
		try:
			print 'Connect to SQL'
			conn = MySQLdb.connect(host="simbalink.com", 
								   user="simbalink", 
								   passwd="simba#903!user", 
								   db="SIMbaLink",
								   connect_timeout=60,
								 )
			print 'Connection Established'
			cursor = conn.cursor()
			cursor.execute(SQL)
			ret = cursor.fetchall()
			cursor.close()
			conn.commit()
			conn.close()
			return ret
		except MySQLdb.Error , e:
			print e.args[0],e.args[1]
			#ret="Error %d: %s".format(e.args[0], e.args[1])
			return False

    def get_shs_id(self,pNum):
		print pNum
		sql = "SELECT `SHSID` \
			 FROM `SolarHomeSystems` \
			 WHERE `SIMNumber`={0}".format(pNum)
		#print "Get SHS ID from Phone Number: " + sql
		return self.execute_sql(sql)

    def get_integer_value(self, queryByteArray, curBitPos, lenBits):
        # Length of PID is 17 bits
        # means the first two bytes plus the first bits of third byte
        startBitPos=curBitPos%8
        curBytePos=curBitPos/8
        if curBitPos == 0: curBytePos =0 
        pid, lenOfWorkingBytes, curWorkingBits=0, 0, 0
        lenOfWorkingBytes=(startBitPos+lenBits)/8+1
        workingByteArray=queryByteArray[curBytePos:
                                     curBytePos+lenOfWorkingBytes]
        for curByteAry in workingByteArray :
            mask=0x80
            while curWorkingBits < lenBits:
                if startBitPos !=0:
                    startBitPos -= 1
                elif curByteAry & mask: 
                    pid+=1
                    pid<<=1
                    curWorkingBits+=1
                else :
                    curWorkingBits+=1
                    pid<<=1
                mask >>= 1
                if mask==0 : break
        return pid>>1    
    
    def get_insert_reading_sql(self, sender, dataList):
		#no_act = [2,3,4,6,7,9,10]
		print 'get insert sql'
		mesg = '{0}'.format(dataList)
		print mesg
		mesg = mesg.replace('[', '').replace(']', '')   
		ret = self.get_shs_id(sender.replace('%2B', ''))
		shsid = str(ret[0][0])
		if int(shsid) <= 10:
			return 'no_act'
		print shsid
		mesg = shsid+', '+mesg
		sql="INSERT INTO `SIMbaLink`.`Readings` \
		   (`SHSID`, `PanelVoltage`, `BatteryVoltage`, `Load1`, \
		  `Load2`, `Load3`,`Load4`,`ReadTime`) \
		   VALUES ({0})".format(mesg)
		return sql  
