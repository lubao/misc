#!/usr/bin/env python
import json
import os
import sys 
import math
import time
ERROR = open('error.log', 'w')
COORD = []
CLOSE = open('group.log','w') 
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

def main():
    import pickle
    COORD = pickle.load(open('all_coord','r'))
    #RES = open('result.log', 'w')
    for i in range(0,len(COORD)-1):
        start = COORD[i]
        dist = []
        k = 0
        while k <= i:
            if k == i:
                dist.append('0')
            else:
                dist.append('-99')
            k += 1
        for j in range(i+1,len(COORD)):
            sys.stdout.write("       \r")
            sys.stdout.write("{0},{1}\r".format(i,j))
            sys.stdout.flush()
            end = COORD[j]
            res = distance(start,end)
            dist.append(res)
            if float(res) < 3.0:
                CLOSE.write('{0},'.format(j))
        #RES.writelines(','.join(dist))
        #RES.writelines('\n')
        CLOSE.writelines('\n')

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


