import requests
import os
import json
from bs4 import BeautifulSoup

data = []

#ham lay du lieu tu trang web duoc chi dinh
def crawlData(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content,"html.parser")
    #Lấy bảng dữ liệu table có class và là bảng đầu tiên, chọn thẻ tr
    links = soup.select('table.conference:last-of-type > tbody >tr')
    
    for link in links:
        #Lấy tất cả thẻ a
        confers = link.find('a').text
        #Lấy thuộc tính href của thẻ a
        confers_link = link.find('a')['href']
        #Tìm tất cả thẻ span /td có thuộc tính class
        # confersdescrip = link.find('span', attrs={'class':'tooltiptext'}).text
        years = link.find('td', attrs={'class':'year'}).text
        locations = link.find('td', attrs={'class':'location'}).text
        startingdates = link.find('td', attrs={'class':'starting-date'}).text
        endingdates = link.find('td', attrs={'class':'ending-date'}).text
        remarks = link.find('td', attrs={'class':'remark'}).text
        #Luu dữ liệu vào data dạng dicts
        data.append({
            "Conference": confers,
            "hrefconf": confers_link, 
            "year": years,
            "location": locations,
            "startingdate": startingdates,
            "endingdate": endingdates,
            "remark": remarks,
        })
        if os.path.exists("data/pdata.json"):
            json_obj = json.dumps(data)
            with open ("data/pdata.json","w") as outfile:
                outfile.write(json_obj)
        else:
            print("The file does not exists")
    return data

#Lay du lieu tu crawlData
crawlData('https://www.lix.polytechnique.fr/~hermann/conf.php')

