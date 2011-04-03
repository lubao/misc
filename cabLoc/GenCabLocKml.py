#!/usr/bin/env python
import json
import os
import sys 
import math
import time
LOC = [l.strip() for l in open('cab_loc.txt','r')]
CITY = ',Hyderabad,Andhra+Pradesh,India'
ERROR = open('coordinate_error.log', 'w')
RES = open('cab_loc.kml', 'w')
COORD = []
def kmlWriteHeader():
    RES.write(
'''<?xml version="1.0" encoding="UTF-8"?>
  <kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
      <name>Cab Loc</name>
      <open>1</open>
      <description></description>
        <Folder>
           <name>Placemarks</name>
             <description>mark your stop places</description>
'''
    ) 

def kmlWriteInfo(name,lat,lon):
    RES.write(
'''
               <Placemark>
                 <name>{0}</name>
                 <Point>
                  <coordinates>
                    {1},{2},0
                  </coordinates>
                 </Point>
               </Placemark>
'''.format(name,lon,lat)
    ) 


def kmlWriteEnd():
    RES.write(
'''
        </Folder>
    </Document>
  </kml>

'''
    ) 

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


# Yahoo Map API
#os.system (
#'''wget "http://api.maps.yahoo.com/ajax/geocode?appid=batchGeocode&qt=1&id=m&qs={0}&noCacheIE=1300409661603" -q -O coordinate '''.format(start))
#cord = open('coordinate', 'r').readlines()
#data = json.loads( 
#    cord[0].split('<!--')[0].lstrip('YGeoCode.getMap(').rstrip(',1);')
#    )
#{u'GeoAddress': u'Ashok Nagar,Andhra Pradesh,India',
#u'GeoID': u'm',
#u'GeoMID': False,
#u'GeoPoint': {u'Lat': 16.48781, u'Lon': 80.679091999999997},
#u'success': 1}
#kmlWriteInfo(
#data['GeoAddress'],
#data['GeoPoint']['Lat'],data['GeoPoint']['Lon'])



def main():
    kmlWriteHeader()
    for i in range(0,len(LOC)):
        start = LOC[i].replace(' ','+')+CITY
        sys.stdout.write("       \r")
        sys.stdout.write("{0}\r".format(i))
        sys.stdout.flush()
        os.system (
        '''wget "http://maps.google.com/maps/geo?output=json&oe=utf-8&q={0}&key=ABQIAAAA9fM6Vg1sNheq6r5IMI6kZRRm2SEPmOspzCQkeVrFMcw587AklxRT0Qzdzdr9LaKyM502xxyDjs6lrA&sensor=false&mapclient=jsapi&hl=en" -q -O coordinate'''.format(start))
        #cod = open('coordinate', 'r').read()
        #data = json.loads(cod.split('(')[1].rstrip(')'))
        data = json.load(open('coordinate','r'))
        if data['Status']['code'] == 200:
            # coodinate = [Latitude , Lontitude,0]
            coordinate = data['Placemark'][0]['Point']['coordinates']
            kmlWriteInfo(data['name'],coordinate[1],coordinate[0])
            COORD.append([coordinate[1],coordinate[0]])
        else:
            ERROR.write(data['name']+'\n')
        time.sleep(2)
    kmlWriteEnd()
    import pickle
    pickle.dump(COORD,open('all_coord','w'))


if __name__ == '__main__':
    main()
