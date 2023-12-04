import play
import requests
from bs4 import BeautifulSoup

x=0
pages=[]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}
y1=""
y2=""
y3=""
y4=""
y5=""
y6=""
y7=""
y8=""
ys1=""
ys2=""
ys3=""
ys4=""
ys5=""
ys6=""
ys7=""
ys8=""
yd1=""
yd2=""
yd3=""
yd4=""
yd5=""
yd6=""
yd7=""
yd8=""
h1=""
h2=""
h3=""
h4=""
h5=""
h6=""
h7=""
h8=""
a1=""
a2=""
a3=""
a4=""
a5=""
a6=""
a7=""
a8=""
sayfa=1
def uyeler():

    play.set_backdrop((43,64,84))
    global y1
    global y2
    global y3
    global y4
    global y5
    global y6
    global y7
    global y8
    global ys1
    global ys2
    global ys3
    global ys4
    global ys5
    global ys6
    global ys7
    global ys8
    global yd1
    global yd2
    global yd3
    global yd4
    global yd5
    global yd6
    global yd7
    global yd8
    global h1
    global h2
    global h3
    global h4
    global h5
    global h6
    global h7
    global h8
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    
    baslik=play.new_text(words="CANLI DÖVİZ",color="white",font_size=75,x=-170,y=260)
    resim1=play.new_image(image="kur1.png",size=13,y=265,x=350)
    resim2=play.new_image(image="kur2.png",size=20,x=-360,y=260)
    k1=play.new_box(color=(77, 105, 137),border_width=0,border_color="grey",y=130,height=50,width=play.screen.width)
    k2=play.new_box(color=(47, 75, 107),border_width=0,border_color="grey",y=80,height=50,width=play.screen.width)
    k3=play.new_box(color=(77, 105, 137),border_width=0,border_color="grey",y=30,height=50,width=play.screen.width)
    k4=play.new_box(color=(47, 75, 107),border_width=0,border_color="grey",y=-20,height=50,width=play.screen.width)
    k5=play.new_box(color=(77, 105, 137),border_width=0,border_color="grey",y=-70,height=50,width=play.screen.width)
    k6=play.new_box(color=(47, 75, 107),border_width=0,border_color="grey",y=-120,height=50,width=play.screen.width)
    k7=play.new_box(color=(77, 105, 137),border_width=0,border_color="grey",y=-170,height=50,width=play.screen.width)
    k8=play.new_box(color=(47, 75, 107),border_width=0,border_color="grey",y=-220,height=50,width=play.screen.width)
    y1=play.new_text(words="",color="white",x=-20,y=140,font_size=20)
    y2=play.new_text(words="",color="white",x=-20,y=90,font_size=20)
    y3=play.new_text(words="",color="white",x=-20,y=40,font_size=20)
    y4=play.new_text(words="",color="white",x=-20,y=-10,font_size=20)
    y5=play.new_text(words="",color="white",x=-20,y=-60,font_size=20)
    y6=play.new_text(words="",color="white",x=-20,y=-110,font_size=20)
    y7=play.new_text(words="",color="white",x=-20,y=-160,font_size=20)
    y8=play.new_text(words="",color="white",x=-20,y=-210,font_size=20)
    ys1=play.new_text(words="",color="white",x=-300,y=148,font_size=16)
    ys2=play.new_text(words="",color="white",x=-300,y=98,font_size=16)
    ys3=play.new_text(words="",color="white",x=-300,y=48,font_size=16)
    ys4=play.new_text(words="",color="white",x=-300,y=-2,font_size=16)
    ys5=play.new_text(words="",color="white",x=-300,y=-52,font_size=16)
    ys6=play.new_text(words="",color="white",x=-300,y=-102,font_size=16)
    ys7=play.new_text(words="",color="white",x=-300,y=-152,font_size=16)
    ys8=play.new_text(words="",color="white",x=-300,y=-202,font_size=16)
    yd1=play.new_text(words="",color="white",y=120,font_size=30)
    yd2=play.new_text(words="",color="white",y=70,font_size=30)
    yd3=play.new_text(words="",color="white",y=20,font_size=30)
    yd4=play.new_text(words="",color="white",y=-30,font_size=30)
    yd5=play.new_text(words="",color="white",y=-80,font_size=30)
    yd6=play.new_text(words="",color="white",y=-130,font_size=30)
    yd7=play.new_text(words="",color="white",y=-180,font_size=30)
    yd8=play.new_text(words="",color="white",y=-230,font_size=30)
    h1=play.new_text(words="",color="white",x=-350,y=140,font_size=40)
    h2=play.new_text(words="",color="white",x=-350,y=90,font_size=40)
    h3=play.new_text(words="",color="white",x=-350,y=40,font_size=40)
    h4=play.new_text(words="",color="white",x=-350,y=-10,font_size=40)
    h5=play.new_text(words="",color="white",x=-350,y=-60,font_size=40)
    h6=play.new_text(words="",color="white",x=-350,y=-110,font_size=40)
    h7=play.new_text(words="",color="white",x=-350,y=-160,font_size=40)
    h8=play.new_text(words="",color="white",x=-350,y=-210,font_size=40)
    a1=play.new_text(words="",color=(0, 224, 255),x=play.screen.left,y=120,font_size=25)
    a2=play.new_text(words="",color=(0, 224, 255),x=play.screen.left,y=70,font_size=25)
    a3=play.new_text(words="",color=(0, 224, 255),x=play.screen.left,y=20,font_size=25)
    a4=play.new_text(words="",color=(0, 224, 255),x=play.screen.left,y=-30,font_size=25)
    a5=play.new_text(words="",color=(0, 224, 255),x=play.screen.left,y=-80,font_size=25)
    a6=play.new_text(words="",color=(0, 224, 255),x=play.screen.left,y=-130,font_size=25)
    a7=play.new_text(words="",color=(0, 224, 255),x=play.screen.left,y=-180,font_size=25)
    a8=play.new_text(words="",color=(0, 224, 255),x=play.screen.left,y=-230,font_size=25)

    bas1=play.new_text(words="ALIŞ",color="black",y=165,x=-140,font_size=30)
    bas2=play.new_text(words="SATIŞ",color="black",y=165,x=-20,font_size=30)
    bas3=play.new_text(words="EN YUKSEK",color="black",y=165,x=110,font_size=30)
    bas4=play.new_text(words="EN DUSUK",color="black",y=165,x=230,font_size=30)
    bas5=play.new_text(words="KAPANIŞ",color="black",y=165,x=340,font_size=30)

    page1=[play.new_circle(y=-270,x=170,size=15,color=(77, 105, 137)),play.new_text(color="white",font_size=30,y=-270,x=170,words="1",)]
    page2=[play.new_circle(y=-270,x=200,size=15,color=(77, 105, 137)),play.new_text(color="white",font_size=30,y=-270,x=200,words="2",)]
    page3=[play.new_circle(y=-270,x=230,size=15,color=(77, 105, 137)),play.new_text(color="white",font_size=30,y=-270,x=230,words="3",)]
    page4=[play.new_circle(y=-270,x=260,size=15,color=(77, 105, 137)),play.new_text(color="white",font_size=30,y=-270,x=260,words="4",)]
    page5=[play.new_circle(y=-270,x=290,size=15,color=(77, 105, 137)),play.new_text(color="white",font_size=30,y=-270,x=290,words="5",)]
    page6=[play.new_circle(y=-270,x=320,size=15,color=(77, 105, 137)),play.new_text(color="white",font_size=30,y=-270,x=320,words="6",)]
    page7=[play.new_circle(y=-270,x=350,size=15,color=(77, 105, 137)),play.new_text(color="white",font_size=30,y=-270,x=350,words="7",)]
    page8=[play.new_circle(y=-270,x=380,size=15,color=(77, 105, 137)),play.new_text(color="white",font_size=30,y=-270,x=380,words="8",)]
    global pages
    pages=[page1,page2,page3,page4,page5,page6,page7,page8]
    bilgi=play.new_text(words="Sayfa geçişleri için klavyeyi kullanabilirsiniz!",color="grey",font_size=25,y=-292)
dovizlerHarf=[]
dovizlerSatir1=[]
dovizlerSatir2=[]
dovizleradi=[]
renkler=[]
dovizlersaat=[]


siteUrl="https://canlidoviz.com/doviz-kurlari"
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
def renkleriSifirla():
    for i in range(8):
        pages[i][0].color=(77, 105, 137)
        pages[i][1].color="white"
def renkAyarla(key):
    renkleriSifirla()
    pages[key-1][0].color=(0, 224, 255)
    pages[key-1][1].color="red"

    




@play.repeat_forever
async def anlik():
    global x
    if x==1:
        global siteUrl
        global dovizlerHarf
        global dovizlerSatir1
        global dovizlerSatir2
        global dovizleradi
        global renkler
        global dovizlersaat
        global sayfa
        dovizlerHarf=[]
        dovizlerSatir1=[]
        dovizlerSatir2=[]
        dovizleradi=[]
        renkler=[]
        dovizlersaat=[]
        
        sayfaCevabi=requests.get(siteUrl,headers=headers)
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
                sekil=""
                if(sekilBul(kurYuzde)==True):
                    sekil="^"
                    renkler.append("green")
                else:
                    sekil="v"
                    renkler.append("red")
                satir1=sekil+"  "+kurYuzde
                satir2="                                    "+kurAlis+"        "+kurSatis+"        "+kurOynama[0]+"      "+kurOynama[1]+"       "+kurOynama[2]
                dovizlerSatir1.append(satir1)
                dovizlerSatir2.append(satir2)
                dovizlerHarf.append(kurharfi)
                dovizleradi.append(kurAdi)
                dovizlersaat.append(kurTime)
        y1.words=dovizlerSatir1[0+(sayfa-1)*7]
        y2.words=dovizlerSatir1[1+(sayfa-1)*7]
        y3.words=dovizlerSatir1[2+(sayfa-1)*7]
        y4.words=dovizlerSatir1[3+(sayfa-1)*7]
        y5.words=dovizlerSatir1[4+(sayfa-1)*7]
        y6.words=dovizlerSatir1[5+(sayfa-1)*7]
        y7.words=dovizlerSatir1[6+(sayfa-1)*7]
        y8.words=dovizlerSatir1[7+(sayfa-1)*7]
        ys1.words=dovizlersaat[0+(sayfa-1)*7]
        ys2.words=dovizlersaat[1+(sayfa-1)*7]
        ys3.words=dovizlersaat[2+(sayfa-1)*7]
        ys4.words=dovizlersaat[3+(sayfa-1)*7]
        ys5.words=dovizlersaat[4+(sayfa-1)*7]
        ys6.words=dovizlersaat[5+(sayfa-1)*7]
        ys7.words=dovizlersaat[6+(sayfa-1)*7]
        ys8.words=dovizlersaat[7+(sayfa-1)*7]
        y1.color=renkler[0+(sayfa-1)*7]
        y2.color=renkler[1+(sayfa-1)*7]
        y3.color=renkler[2+(sayfa-1)*7]
        y4.color=renkler[3+(sayfa-1)*7]
        y5.color=renkler[4+(sayfa-1)*7]
        y6.color=renkler[5+(sayfa-1)*7]
        y7.color=renkler[5+(sayfa-1)*7]
        y8.color=renkler[6+(sayfa-1)*7]
        yd1.words=dovizlerSatir2[0+(sayfa-1)*7]
        yd2.words=dovizlerSatir2[1+(sayfa-1)*7]
        yd3.words=dovizlerSatir2[2+(sayfa-1)*7]
        yd4.words=dovizlerSatir2[3+(sayfa-1)*7]
        yd5.words=dovizlerSatir2[4+(sayfa-1)*7]
        yd6.words=dovizlerSatir2[5+(sayfa-1)*7]
        yd7.words=dovizlerSatir2[6+(sayfa-1)*7]
        yd8.words=dovizlerSatir2[7+(sayfa-1)*7]
        h1.words=dovizlerHarf[0+(sayfa-1)*7]
        h2.words=dovizlerHarf[1+(sayfa-1)*7]
        h3.words=dovizlerHarf[2+(sayfa-1)*7]
        h4.words=dovizlerHarf[3+(sayfa-1)*7]
        h5.words=dovizlerHarf[4+(sayfa-1)*7]
        h6.words=dovizlerHarf[5+(sayfa-1)*7]
        h7.words=dovizlerHarf[6+(sayfa-1)*7]
        h8.words=dovizlerHarf[7+(sayfa-1)*7]
        a1.words=dovizleradi[0+(sayfa-1)*7]
        a2.words=dovizleradi[1+(sayfa-1)*7]
        a3.words=dovizleradi[2+(sayfa-1)*7]
        a4.words=dovizleradi[3+(sayfa-1)*7]
        a5.words=dovizleradi[4+(sayfa-1)*7]
        a6.words=dovizleradi[5+(sayfa-1)*7]
        a7.words=dovizleradi[6+(sayfa-1)*7]
        a8.words=dovizleradi[7+(sayfa-1)*7]
        if a1.words=="Dolar":
            a1.x=play.screen.left+2*a1.size
            a2.x=play.screen.left+2*a2.size
        else:
            a1.x=play.screen.left+a1.size
            a2.x=play.screen.left+a2.size

        a3.x=play.screen.left+a3.size
        a4.x=play.screen.left+a4.size
        a5.x=play.screen.left+a5.size
        a6.x=play.screen.left+a6.size
        a7.x=play.screen.left+a7.size
        a8.x=play.screen.left+a8.size
        

@play.when_any_key_pressed
async def sayfaDegis(key):
    global sayfa
    if key=="1" or key=="2" or key=="3" or key=="4" or key=="5" or key=="6" or key=="7" or key=="8":
        key=int(key)
        sayfa=key
        renkAyarla(key)
        y1.words=dovizlerSatir1[0+(sayfa-1)*7]
        y2.words=dovizlerSatir1[1+(sayfa-1)*7]
        y3.words=dovizlerSatir1[2+(sayfa-1)*7]
        y4.words=dovizlerSatir1[3+(sayfa-1)*7]
        y5.words=dovizlerSatir1[4+(sayfa-1)*7]
        y6.words=dovizlerSatir1[5+(sayfa-1)*7]
        y7.words=dovizlerSatir1[6+(sayfa-1)*7]
        y8.words=dovizlerSatir1[7+(sayfa-1)*7]
        ys1.words=dovizlersaat[0+(sayfa-1)*7]
        ys2.words=dovizlersaat[1+(sayfa-1)*7]
        ys3.words=dovizlersaat[2+(sayfa-1)*7]
        ys4.words=dovizlersaat[3+(sayfa-1)*7]
        ys5.words=dovizlersaat[4+(sayfa-1)*7]
        ys6.words=dovizlersaat[5+(sayfa-1)*7]
        ys7.words=dovizlersaat[6+(sayfa-1)*7]
        ys8.words=dovizlersaat[7+(sayfa-1)*7]
        y1.color=renkler[0+(sayfa-1)*7]
        y2.color=renkler[1+(sayfa-1)*7]
        y3.color=renkler[2+(sayfa-1)*7]
        y4.color=renkler[3+(sayfa-1)*7]
        y5.color=renkler[4+(sayfa-1)*7]
        y6.color=renkler[5+(sayfa-1)*7]
        y7.color=renkler[5+(sayfa-1)*7]
        y8.color=renkler[6+(sayfa-1)*7]
        yd1.words=dovizlerSatir2[0+(sayfa-1)*7]
        yd2.words=dovizlerSatir2[1+(sayfa-1)*7]
        yd3.words=dovizlerSatir2[2+(sayfa-1)*7]
        yd4.words=dovizlerSatir2[3+(sayfa-1)*7]
        yd5.words=dovizlerSatir2[4+(sayfa-1)*7]
        yd6.words=dovizlerSatir2[5+(sayfa-1)*7]
        yd7.words=dovizlerSatir2[6+(sayfa-1)*7]
        yd8.words=dovizlerSatir2[7+(sayfa-1)*7]
        h1.words=dovizlerHarf[0+(sayfa-1)*7]
        h2.words=dovizlerHarf[1+(sayfa-1)*7]
        h3.words=dovizlerHarf[2+(sayfa-1)*7]
        h4.words=dovizlerHarf[3+(sayfa-1)*7]
        h5.words=dovizlerHarf[4+(sayfa-1)*7]
        h6.words=dovizlerHarf[5+(sayfa-1)*7]
        h7.words=dovizlerHarf[6+(sayfa-1)*7]
        h8.words=dovizlerHarf[7+(sayfa-1)*7]
        a1.words=dovizleradi[0+(sayfa-1)*7]
        a2.words=dovizleradi[1+(sayfa-1)*7]
        a3.words=dovizleradi[2+(sayfa-1)*7]
        a4.words=dovizleradi[3+(sayfa-1)*7]
        a5.words=dovizleradi[4+(sayfa-1)*7]
        a6.words=dovizleradi[5+(sayfa-1)*7]
        a7.words=dovizleradi[6+(sayfa-1)*7]
        a8.words=dovizleradi[7+(sayfa-1)*7]


@play.when_program_starts
async def anim(): 
    resim4=play.new_image(image="dov.png",size=120)
    yazi1=play.new_text(words="CANLI",color="white",y=40,font_size=100)
    yazi2=play.new_text(words="DÖVİZ",y=-50,color="white",font_size=100)
    resim3=play.new_image(image="kur2.png",)
    
    await play.timer(1)
    for i in range(250):
        yazi1.go_to(x=i*(-1),y=40)
        await play.animate()
    for i in range(250):
        yazi2.go_to(x=i,y=-50)
        await play.animate()
    await play.timer(0.7)
    yazi2.angle=-50
    await play.animate()
    yazi1.start_physics()
    yazi2.start_physics()
    resim3.start_physics()
    await play.timer(3)

    yazi1.remove()
    yazi2.remove()
    resim3.remove()
    resim4.remove()
    global x
    x=1
    uyeler()
    
        
        

    

play.start_program()