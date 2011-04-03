#!/usr/bin/env python
import json
import os
import sys 
import math
import time
import pickle
CENTER = [78.4756,17.4359]
CENTER_FOR_DIST = [ 17.4359,78.4756]
COORD = pickle.load(open('all_coord','r'))
AREA = [l.strip() for l in open('cab_loc.txt','r')]
ERROR = open('error.log', 'w')
ALL = [[],]
CLOSE = open('group.log','w') 
XML = open('ad.tmp','w') 
SCHEMA_ID = 0
STATUS = ['On Duty','Off Duty']
DIVID = []

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(float(lat2)-float(lat1))
    dlon = math.radians(float(lon2)-float(lon1))
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return str(round(d,2))

def WriteAppXML(loc):
    global SCHEMA_ID
    name = loc.pop(0)
    XML.write(
    '''<schema id="{0}" name="{1}">\n'''.format(SCHEMA_ID,name))
    XML.write(
    '''\t<fields total="3" primary_field_id="0">\n''')
    # ID field
    XML.write(
    '''\t\t<field id="0" name="Driver ID" range="16"/>\n''')
    # Area field
    XML.write(
    '''\t\t<field id="1" name="Area" range="-3">\n''')
    XML.write(
    '''\t\t\t<choices total="{0}">\n'''.format(len(loc)))
    for l in loc:
        XML.write(
        '''\t\t\t\t<choice name="{0}"/>\n'''.format(AREA[l]))
    XML.write(
    '''\t\t\t</choices>\n''')
    XML.write(
    '''\t\t</field>\n''')
    # Status field
#    XML.write(
#    '''\t\t<field id="2" name="Status" range="-3">\n''')
#    XML.write(
#    '''\t\t\t<choices total="{0}">\n'''.format(len(STATUS)))
#    for l in STATUS:
#        XML.write(
#        '''\t\t\t\t<choice name="{0}"/>\n'''.format(l))
#    XML.write(
#    '''\t\t\t</choices>\n''')
#    XML.write(
#    '''\t\t</field>\n''')
    # ETA field
    XML.write(
    '''\t\t<field id="2" name="Duration" range="8"/>\n''')
    XML.write(
    '''\t</fields>\n''')
    XML.write(
    '''</schema>\n''')
    FXML = open('{0}.xml'.format(SCHEMA_ID),'w') 
    FXML.write(
'''<?xml version="1.0" encoding="UTF-8" ?>
<form id="{0}" application="0" operation="1" name="{1}">
    <table>
        <schemas total="1">
            <schema id="{0}">
                <fields total="3">
                    <field id="0"/>
                    <field id="1"/>
                    <field id="2"/>
                </fields>
            </schema>
        </schemas>
    </table>
</form>'''.format(SCHEMA_ID,name))
    SCHEMA_ID += 1

def dividArea(point):
    prefix = point.pop(0)
    nw = [prefix+'North West']
    ne = [prefix+'North East']
    sw = [prefix+'South West']
    se = [prefix+'South East']
    for i in point:
        y,x = COORD[i]
        if x <= CENTER[0] and y <= CENTER[1]: sw.append(i)
        if x <= CENTER[0] and y >= CENTER[1]: nw.append(i)
        if x >= CENTER[0] and y <= CENTER[1]: se.append(i)
        if x >= CENTER[0] and y >= CENTER[1]: ne.append(i)
    for l in [nw, ne, sw, se]:
        WriteAppXML(l)


CENTRA = ['Centra ']
OUTSKIRT = ['Outskirt ']

def seperate():
    for i in range(0,len(COORD)-1):
        start = COORD[i]
        res = distance(start,CENTER_FOR_DIST)
        if float(res) < 8.0:
            CENTRA.append(i)
        else:
            OUTSKIRT.append(i)
    for l in [CENTRA, OUTSKIRT]:
        print l
        dividArea(l)

def main():
    seperate()
#    dividArea()
#    for i in range(0,len(COORD)-1):
#        skip =False
#    	for c in ALL:
#            if i in c: skip = True
#        if not skip:
#            start = COORD[i]
#            tmp = [i]
#            for j in range(i+1,len(COORD)):
#                skip =False
#                for c in ALL:
#                    if j in c: skip = True
#                if not skip:
#                    end = COORD[j]
#                    res = distance(start,end)
#                    if float(res) < 12.0 and float(res) > 0.0 and len(tmp) < 15:
#                        tmp.append(j)
#            ALL.append(tmp)
#            name = AREA[tmp[0]] 
#            tmp.insert(0,name)
#            WriteAppXML(tmp)
#            CLOSE.writelines(''.join(str(tmp).strip()))
#            CLOSE.writelines('\n')

if __name__ == '__main__':
    main()

# Yahoo Map API
#def getCoordinate():
#    for i in range(0,len(LOC)):
#        start = LOC[i].replace(' ','+')+CITY
#        sys.stdout.write("       \r")
#        sys.stdout.write("{0}\r".format(i))
#        sys.stdout.flush()
#        os.system (
#'''wget "http://api.maps.yahoo.com/ajax/geocode?appid=batchGeocode&qt=1&id=m&qs={0}&noCacheIE=1300409661603" -q -O coordinate '''.format(start))
#        cord = open('coordinate', 'r').readlines()
#        data = json.loads(
#            cord[0].split('<!--')[0].lstrip('YGeoCode.getMap(').rstrip(',1);')
#        )
#        COORD.append([data['GeoPoint']['Lat'],data['GeoPoint']['Lon']])
#        time.sleep(1)
#    import pickle
#    pickle.dump(COORD,open('all_coord','w'))

# Google Map API
#end = LOC[j].replace(' ','+')+CITY
#os.system (
#'''wget "http://maps.googleapis.com/maps/api/directions/
#json?origin={0}&destination={1}&sensor=false" -q -O route'''.format(start,end))
#if res == '-1.0':
#ERROR.writelines(str(j+1)+' : '+end+'\n')
#time.sleep(5)
#def getDistance():
#    DIST = 0.0
#    root = json.load(open('route','r'))
#    dist = 0.0
#    if root['status'] == 'OK':
#        legs = root['routes'][0]['legs']
#        for leg in legs:
#            for s in leg['steps']:
#                dis = s['distance']['text'].split(' ')
#                if dis[1] == 'm':
#                    dis[0] = (float(dis[0])/1000.0)
#                DIST += float(dis[0])
#    else:
#        ERROR.writelines(root['status']+'\n')
#        DIST = -1.0
#    return str(round(DIST,2))


