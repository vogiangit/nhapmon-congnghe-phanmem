import requests
import os
import json
from bs4 import BeautifulSoup

URL = 'https://www.lix.polytechnique.fr/~hermann/conf.php#'

resq = requests.get(URL)
soup = BeautifulSoup(resq.content,"html.parser")

pages = soup.select('table.conference:nth-of-type(2) > tbody >tr')

Outdata =[]
for running in pages:
        confer_running = running.find('a').text
        confer_link = running.find('a')['href']
        location_running = running.find('td', attrs={'class':'location'}).text
        date_running = running.find('td', attrs={'class':'running-date'}).text     
        remark_running = running.find('td', attrs={'class':'remark'}).text
     
        Outdata.append({
               "Conference": confer_running,
               "hrefconf": confer_link,
                "Location": location_running,
                "Date": date_running,
                "Remark": remark_running
        })
        print(Outdata)
        if os.path.exists("NMCNPM/data/rdata.json"):
            json_obj = json.dumps(Outdata)
            with open ("NMCNPM/data/rdata.json","w") as Datarun:
                Datarun.write(json_obj)
        else:
            print("The file does not exists")






    