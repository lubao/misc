import MySQLdb

class SQLEng():
    
    def exeSQL(self,SQL):
        try:
            conn=MySQLdb.connect(host="localhost",
                                 user="root",
                                 passwd="hello",
                                 )
            cursor=conn.cursor()
            cursor.execute(SQL)
            ret=cursor.fetchall()
            cursor.close()
            conn.commit()
            conn.close()
            return ret
        except MySQLdb.Error ,e:
            #ret="Error %d: %s".format(e.args[0],e.args[1])
            return False
    
    def getMsg(self,id):
        SQL="""
            SELECT `Text` , `SenderNumber` , `UDH`
            FROM `smsd`.`inbox`
            WHERE ID ={0}
            """.format(id)
        return self.exeSQL(SQL)
            
    def getInsetSentBoxMsg(self,to,mesg):
        return '''
            INSERT INTO `smsd`.`outbox` (
            `UpdatedInDB` ,
            `InsertIntoDB` ,
            `SendingDateTime` ,
            `Text` ,
            `DestinationNumber` ,
            `Coding` ,
            `UDH` ,
            `Class` ,
            `TextDecoded` ,
            `ID` ,
            `MultiPart` ,
            `RelativeValidity` ,
            `SenderID` ,
            `SendingTimeOut` ,
            `DeliveryReport` ,
            `CreatorID`
            )
            VALUES (
            CURRENT_TIMESTAMP , 
            '0000-00-00 00:00:00', 
            '0000-00-00 00:00:00', 
            '', '{1}', 'Default_No_Compression', '', 
            '-1', '{0}', NULL , 'false', '-1', NULL , 
            '0000-00-00 00:00:00', 'default', ''
            )'''.format(mesg,to)