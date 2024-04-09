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
    links = soup.select('table.conference:first-of-type > tbody >tr')
    
    for link in links:
        #Lấy tất cả thẻ a
        confers = link.find('a').text
        confers_link = link.find('a')['href']
        #Tìm tất cả thẻ span /td có thuộc tính class
        # confersdescrip = link.find('span', attrs={'class':'tooltiptext'}).text
        locations = link.find('td', attrs={'class':'location'}).text
        #truong hop loi, chon class khac
        try:
            deadlines = link.find('td', attrs={'class':'now-deadline'}).text
        except:
            deadlines = link.find('td', attrs={'class':'deadline'}).text
        dates = link.find('td', attrs={'class':'date'}).text
        notifications = link.find('td', attrs={'class':'notification'}).text
        subformats = link.find('td', attrs={'class':'subformat'}).text
        #Luu dữ liệu vào data dạng dicts
        data.append({
            "Conference": confers,
            "ConferLink": confers_link, 
            "Location": locations,
            "Deadline": deadlines,
            "Date": dates,
            "Notification": notifications,
            "Subformat": subformats,
        })
        if os.path.exists("data/ddata.json"):
            json_obj = json.dumps(data)
            with open ("data/ddata.json","w") as outfile:
                outfile.write(json_obj)
        else:
            print("The file does not exists")
    return data

#Lay du lieu tu crawlData
#crawlData('https://www.lix.polytechnique.fr/~hermann/conf.php#ahead')
crawlData('https://www.lix.polytechnique.fr/~hermann/conf.php')

