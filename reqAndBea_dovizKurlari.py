import requests
from bs4 import BeautifulSoup
import time

siteUrl="https://canlidoviz.com/doviz-kurlari"

sayfaCevabi=requests.get(siteUrl)

def boslukEkle(a,s):
    for x in range(s):
            if(len(a)!=s):
                a+=" "
            else:
                continue
    return a
def sekilBul(a):
        sayac=0
        sekil=False
        for i in a:
            if i=="%":
                sayac+=1
            if sayac==1 and i=="-":
                sekil=False
                break
            else:
                sekil=True
                
        return sekil
while(True):
    if sayfaCevabi.status_code==200:
        htmlIcerik=sayfaCevabi.content
        soup=BeautifulSoup(htmlIcerik,"html.parser")
        for kurlar in soup.find_all("tr",{"data-type":"detail"}):
            kurharfi=kurlar.find("a").text.strip("\n \t")[0:6]
            kurAdi=kurlar.find("div",{"class":"highlight"}).text.strip(" ")
            kurAdi=boslukEkle(kurAdi,21)
            kurTime=kurlar.find("span").text
            kurAlis=kurlar.find("td",{"class":"text-primary text-right text-title"}).text.strip("\n \t")
            kurAlis=boslukEkle(kurAlis,8)
            kurSatis=kurlar.find("td",{"class":"text-right"}).text.strip("\n \t")[0:8]
            kurSatis=boslukEkle(kurSatis,8)
            kurOynama=[]
            kurYuzde=kurlar.find("div",{"class":"status-row"}).text.strip("\n \t")
            
            for i in kurlar.find_all("td",{"class":"text-primary text-right text-title hidden-sm"}):
                i=i.text.strip("\n \t")
                i=boslukEkle(i,8)
                kurOynama.append(i)
            bosluk=""
            bosluk2=""
            bosluk3=""
            bosluk4=""
            bosluk5=""
            bosluk6=""
            bosluk6=boslukEkle(bosluk6,31)
            bosluk=boslukEkle(bosluk,5)
            bosluk2=boslukEkle(bosluk2,8)
            bosluk3=boslukEkle(bosluk3,7)
            bosluk4=boslukEkle(bosluk4,3)
            bosluk5=boslukEkle(bosluk5,4)
            sekil=""
            if(sekilBul(kurYuzde)==True):
                sekil="▲"
            else:
                sekil="▼"


            print(kurharfi+"   "+kurTime+"'"+bosluk+"ALIS"+bosluk2+"SATIS"+bosluk3+"EN YUKSEK"+bosluk4+"EN DUSUK"+bosluk5+"KAPANIS") 
            print(kurAdi+"  "+kurAlis+"    "+kurSatis+"    "+kurOynama[0]+"    "+kurOynama[1]+"    "+kurOynama[2])
            print(bosluk6+sekil+"  "+kurYuzde)
            print("\n---------------------------------------------------------------------------------\n")
        time.sleep(15)
    #▲ ▼


    else:
        print("Sayfaya ulasilamiyor!")





