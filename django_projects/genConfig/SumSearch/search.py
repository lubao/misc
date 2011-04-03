#!/usr/bin/env python

import sys
import re
import os
import commands

ranks = []
results = []

pattern = re.compile("(\d+)")

def extractDate(text):
    p = text.split()
    size = len(p)
    for i in range(0,size):
        if p[i].find('200') != -1 or p[i].find('199') != -1:
            p[i] = p[i].replace(',','')
            p[i] = p[i].replace('.','')
            p[i] = p[i].replace('!','')
            p[i] = p[i].replace(':','')
            p[i] = p[i].replace(';','')
            match = re.search(pattern,p[i])
            if match:
                ret = int(match.groups()[0])
            else:
                ret = -1
            return ret

def extractPrice(text):
    found = 0
    p = text.split()
    size = len(p)
    for i in range(0,size):
        if p[i].find('$') != -1:
            found = 1
            if len(p[i]) == 1:
                price = p[i+1]
            else:
                price = p[i]
        
    if found == 0:
        return '-1'
    price = price.replace('$','')
    price = price.replace(',','')
    price = price.replace('k','000')

    match = re.search(pattern,price)
    if match:
        ret = int(match.groups()[0])
    else:
        ret = -1
    return ret
        
def insert_into_list(txt,num):
    i = 0;
    print i
    if len(ranks) > 0:
        print len(ranks)
        while num < ranks[i]:
            i = i + 1
            if i == len(ranks):
                ranks.append(num)
                results.append(txt)
                return
    ranks.insert(i,num)
    results.insert(i,txt)

make = str(sys.argv[1])
yearstart = int(sys.argv[2])
yearend = int(sys.argv[3])
pricestart = int(sys.argv[4])
priceend = int(sys.argv[5])
source = open(sys.argv[6], 'r')

ad = ''
success = ''
line = ''
#print "how"

def foo(fh):
    lines = [l.strip() for l in fh.readlines()] #fh.readlines() #
    begDelim = [i for i,l in enumerate(lines) if  "---"==l]
    endDelim = [i for i,l in enumerate(lines) if  "***"==l]
    assert(len(begDelim) == len(endDelim))
    adsAsLines = [lines[begDelim[i]+1:endDelim[i]] for i,e in enumerate(begDelim)]
    ads = ["".join(ad) for ad in adsAsLines]
    return ads

#sys.exit(0)

def callThis():
    allAds    = foo(source)
    allLowAds = [ad.lower() for ad in allAds]

    adRanks = [0 for i in xrange(0,len(allAds))]
    for i,ad in enumerate(allLowAds):
        # "Make" match
        if ad.find(make.lower()) != -1:
            adRanks[i] += 5

            # "Date" match
            date = extractDate(ad)
            if date >= yearstart and date <= yearend:
                adRanks[i] += 1

            # "Price" match
            price = extractPrice(ad)
            if price >= pricestart and price <= priceend:
                adRanks[i] += 1
            else:
                adRanks[i] -= 10

    adsRanks = zip(allAds,adRanks)
    adsRanks.sort(lambda x,y: cmp(int(x[1]),int(y[1])))
    adsRanks.reverse()

    toPrint = [e for e in adsRanks if e[1] >= 5]

    ret = ""
    for e in toPrint:
        ret += "<p>%s" % (e[0])
    print ret

    #print adRanks

callThis()

# print "what"
# for i in range(0,101):
#     ad = ''
#     line = source.readline()
#     print line
#     while line.find('---') != -1:
#         line = source.readline()
#         print line

#     while line.find('***') == -1:
#         line = source.readline()
#         ad = ad + line

#     lowad = ad.lower()           
#     if lowad.find("Honda") != -1:
#         rank = 0
#         success = success + ad
#         date = extractDate(ad)
#         if date >= yearstart and date <= yearend:
#             rank = rank + 1;
#         print '-------->' + str(date)
#         price = extractPrice(ad)
#         if price >= pricestart and price <= priceend:
#             rank = rank + 1;
#         #success = success + '\nRank: ' + str(rank) + '\n'
#         insert_into_list(ad,rank) 
#         #ranks.append(rank)
#         #results.append(ad)
#         print '$$$$: ' + str(price)
        
# #print success
# #print ranks
# print results


