import requests
import os
import json
from bs4 import BeautifulSoup
data= []  
def findTag_a(column,row):
    if column.find('a'):
        return column.find('a')['href']
    else:
        return None    
resp = requests.get('https://www.lix.polytechnique.fr/~hermann/conf.php') #source code
soup = BeautifulSoup(resp.content,"html.parser")

#print(soup)
#confname_a = soup.select('table.conference >tbody > tr >td.confname >a')
#for link in confname_a:
    #print(link.text) # in noi dung
    #print (link['href']) # in url

#table = soup.find('table:third-of-type',class_='conference')
#extract the rows of the table 
#rows = table.find('tr') #Search tag td in table
rows = soup.select('table.conference:nth-of-type(3) > tbody >tr')
#print(rows)
for row_id,row in enumerate(rows):  
    columns=row.find_all('td')
#     #print(f"row:{row_id}: {columns}") #row[0] = null
    if columns:
        fName=columns[0].text.strip().split('\n')
        fName=' '.join(fName[:-1]) #cut tag span
        fName_link=findTag_a(columns[0],row_id)
        print(f"Link name: {fName_link}")
        fLocation=columns[1].text.strip() 
        fDate=columns[2].text.strip()
        fNoti=columns[3].text.strip()
        fFinal=columns[4].text.strip() 
        fRegistration=columns[5].text.strip()
        fRemark_link=findTag_a(columns[6],row_id)   
        print(fRemark_link) 
        fRemark=columns[6].text.strip()
        data.append({
            "Name": fName,
            "Location": fLocation,
            "Date": fDate ,
            "Notification": fNoti,
            "Final": fFinal,
            "Registration": fRegistration,
            "Remark":fRemark,
            "LinkName": fName_link,
        })
        print(data)
    if os.path.exists("NMCNPM/data/fdata.json"):
        jsonfile=open("NMCNPM/data/fdata.json","w")
        json.dump(data,jsonfile)
        jsonfile.close()
    else: 
        print("The file does not exists")
