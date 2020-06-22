from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon='C:/Users/hp/Downloads/notify.ico',
        timeout=6
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__=='__main__':
    while True:
        notifyMe('renu','lets stop this virus')
        myhtmlData=getData('https://www.mohfw.gov.in/')
        #print(myhtmlData)
        soup=BeautifulSoup(myhtmlData,'html.parser')
        mydatastr=""
        #print(soup.prettify())
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mydatastr += tr.get_text()
        mydatastr=mydatastr[1:]
        itemList=mydatastr.split("\n\n")
        states=['Maharashtra','Uttar Pradesh','Delhi']
        for item in itemList[0:35]:
            dataList=item.split("\n")
            if dataList[1] in states:
                print(dataList)
                nTitle="cases of Covid-19"
                nText=f"state {dataList[1]}\nActive Cases: {dataList[2]} & Cured: {dataList[3]}\n Deaths: {dataList[4]}\n Total Cases: {dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep(3600)

