import json 
import requests
import urllib.request as urllib
import pandas as pd
from sqlite3 import dbapi2 as sq3
import os

url="https://api.coursera.org/api/courses.v1?start="+"1"+"01&fields=startDate,categories,previewLink,description,photoUrl"
data = urllib.urlopen(url).read()
dataDict = json.loads(data.decode('utf-8'))
print (type(dataDict['elements']))

i=0;
coursera=[];
while 1:    
    url="https://api.coursera.org/api/courses.v1?start="+str(i)+"01&fields=startDate,categories,previewLink,description,photoUrl"
    try:
        data = urllib.urlopen(url).read()
    except URLError as e:
        continue
    dataDict = json.loads(data.decode('utf-8'))
    with open('data.txt', 'a') as outfile:
        json.dump(dataDict, outfile)
    if(dataDict['elements'] == []):
        break
    coursera=coursera+dataDict['elements']
    i=i+1
    print ("Pages scraped",i)

print (len(coursera))
print coursera[0].keys()
#startDate=[m['startDate'] for m in coursera]

startDate=[]
for m in coursera:
    try:
        startDate.append(m['startDate'])
    except KeyError as k:
        startDate.append(None)
print (len(startDate))

coursera=pd.DataFrame(coursera)
print (coursera.head())