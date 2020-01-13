# import libraries
import requests
import urllib.request
from bs4 import BeautifulSoup
from calendar import month_name
import re
import csv
import datetime

#Formatting the scraped date info into ISO format
def dateInDesiredFormat(text):
   data_split=text.split()
   dateInWords=''
   dateInISO=''
   for index,word in enumerate(data_split):
      if index==1:
         currentWord=word
         pattern = '|'.join(month_name[1:])
         currentWord=re.search(pattern, currentWord, re.IGNORECASE).group(0)
         if currentWord in (month_name[1:]):
               currMonth=month_name[1:].index(currentWord)
               dateInWords= data_split[index-1]+currentWord
               dateInISO= datetime.datetime(2019,currMonth+1,int(data_split[index-1]),0,0,0) 
   return dateInISO.strftime("%Y-%m-%dT%H:%M:%S+00:00")

# specify the url and access the site
url = "https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches"
response = requests.get(url).text

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(response, "html.parser")

#print(soup.prettify())

# Inspecting element and finding that the tables fall under sortable
My_table = soup.find('table',{'class':'wikitable collapsible'})

#print(My_table.prettify())

#Extracting all table rows
allrows = My_table.findAll('tr')

list_of_launches=[]

for row in allrows:
    td = row.find_all('td')
    datarow = [i.text for i in td]
    if len(datarow)==5 or len(datarow)==6:
       list_of_launches.append(datarow)

list_of_launches=list_of_launches[1:]

dict_of_launches={}

currDateOfLaunch=''
currVesselOnDate=0

for row in list_of_launches:
   if(len(row)==5):
      rowDate=dateInDesiredFormat(row[0]) 

      if rowDate==currDateOfLaunch:
         currVesselOnDate+=1
         currDateOfLaunch=rowDate
      else:
         currVesselOnDate=1
         currDateOfLaunch=rowDate
         dict_of_launches[currDateOfLaunch]={}

      dict_of_launches[currDateOfLaunch][currVesselOnDate]=0

   if(len(row)==6):
      if (dict_of_launches[currDateOfLaunch][currVesselOnDate]==0):
         launchStatus = row[5]
         launchStatus = re.sub(r'[^a-zA-Z ]+', '', launchStatus)
         if launchStatus in ['Successful','Operational','En route']:
            dict_of_launches[currDateOfLaunch][currVesselOnDate]=1

#import json
#print(json.dumps(dict_of_launches))

# open a csv file with append, so old data will not be erased
with open('launches.csv', 'w') as csv_file:
   writer = csv.writer(csv_file)
   writer.writerow(['date', 'value'])
   date = datetime.datetime(2019,1,1,0,0,0)

   for i in range(0,365):
      if date.strftime("%Y-%m-%dT%H:%M:%S+00:00") not in dict_of_launches.keys():
         writer.writerow([date.strftime("%Y-%m-%dT%H:%M:%S+00:00"), 0])
         date += datetime.timedelta(days=1)

      #for launchdate in dict_of_launches.keys():
      else:
         launchdate=date.strftime("%Y-%m-%dT%H:%M:%S+00:00")
         successfullaunches=0
         for launchvessel in dict_of_launches[launchdate]:
            if dict_of_launches[launchdate][launchvessel]==1:
               successfullaunches+=1
         writer.writerow([launchdate, successfullaunches])
         date += datetime.timedelta(days=1)
