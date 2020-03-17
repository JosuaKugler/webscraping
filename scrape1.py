import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import passwds

def get_html(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8", errors = "replace")
    fp.close()
    return mystr

def get_soup(url):
    return BeautifulSoup(get_html(url), "html.parser")

def physicslogin():
    os.system("wmctrl -a firefox")
    time.sleep(1)
    uniid = passwds.uniid()
    passwd = passwds.passwd()
    os.system("xdotool key "+ uniid + " Return")
    os.system("xdotool key -delay 5 " + passwd + " Return")



#monday and wednesday evening
def get_ex1_content():
    soup = get_soup("https://uebungen.physik.uni-heidelberg.de/vorlesung/20192/pep1")
    #print(soup.prettify())
    body = soup.body
    divlist = body.find_all('div')
    for div in divlist:
        try:
            if div["id"] == "infoarea-6444":
                materialien = div
                break
        except:
            pass

    prelinklist = materialien.find_all('a')
    linklist = []
    for prelink in prelinklist:
        link = "https://uebungen.physik.uni-heidelberg.de" + prelink['href']
        if "pdflink" in prelink['class']:
            linklist.append(link)
    #already in folder Downloads
    predownloadcontents = os.listdir("/home/josua/Downloads")
    #already in folder uni/ex
    alreadydownloaded = os.listdir("/home/josua/uni/ex/")
    links = linklist
    newlinks = []
    for link in links:
        splitlink = link.split("/")
        name = splitlink[-1]
        if name not in alreadydownloaded:
            newlinks.append(link)
    for link in newlinks:
        os.system("firefox -new-tab "+link)
        physicslogin()
        os.system("xdotool key Ctrl+w")
    afterdownloadcontents = os.listdir("/home/josua/Downloads")
    for file in afterdownloadcontents:
        if file not in predownloadcontents:
            os.chdir("/home/josua/Downloads")
            print("mv " + file + " /home/josua/uni/ex/")
            os.system("mv " + file + " /home/josua/uni/ex/")

#mondays after 11:30
def get_theo1_zettel():
    soup = get_soup("https://uebungen.physik.uni-heidelberg.de/vorlesung/20192/1058")
    #print(soup.prettify())
    body = soup.body
    divlist = body.find_all('div')
    for div in divlist:
        try:
            if div["id"] == "infoarea-6191":
                zettel = div
                break
        except:
            pass

    prelinklist = zettel.find_all('a')
    linklist = []
    for prelink in prelinklist:
        link = "https://uebungen.physik.uni-heidelberg.de" + prelink['href']
        if "pdflink" in prelink['class']:
            linklist.append(link)
    #already in folder Downloads
    predownloadcontents = os.listdir("/home/josua/Downloads")
    #already in folder uni/ex
    alreadydownloaded = os.listdir("/home/josua/uni/theo/zettel")
    links = linklist
    newlinks = []
    for link in links:
        splitlink = link.split("/")
        name = splitlink[-1]
        if name not in alreadydownloaded:
            newlinks.append(link)
    for link in newlinks:
        os.system("firefox -new-tab "+link)
        physicslogin()
        os.system("xdotool key Ctrl+w")
    afterdownloadcontents = os.listdir("/home/josua/Downloads")
    for file in afterdownloadcontents:
        if file not in predownloadcontents:
            os.chdir("/home/josua/Downloads")
            print("mv " + file + " /home/josua/uni/theo/zettel")
            os.system("mv " + file + " /home/josua/uni/theo/zettel")

#thursday evening
def get_ex1_zettel():
    soup = get_soup("https://uebungen.physik.uni-heidelberg.de/vorlesung/20192/pep1")
    #print(soup.prettify())
    body = soup.body
    divlist = body.find_all('div')
    for div in divlist:
        try:
            if div["id"] == "infoarea-6406":
                zettel = div
                break
        except:
            pass

    prelinklist = zettel.find_all('a')
    linklist = []
    for prelink in prelinklist:
        link = "https://uebungen.physik.uni-heidelberg.de" + prelink['href']
        if "pdflink" in prelink['class']:
            linklist.append(link)
    #already in folder Downloads
    predownloadcontents = os.listdir("/home/josua/Downloads")
    #already in folder uni/ex
    alreadydownloaded = os.listdir("/home/josua/uni/ex/zettel")
    links = linklist
    newlinks = []
    for link in links:
        splitlink = link.split("/")
        name = splitlink[-1]
        if name not in alreadydownloaded:
            newlinks.append(link)
    for link in newlinks:
        os.system("firefox -new-tab "+link)
        physicslogin()
        os.system("xdotool key Ctrl+w")
    afterdownloadcontents = os.listdir("/home/josua/Downloads")
    for file in afterdownloadcontents:
        if file not in predownloadcontents:
            os.chdir("/home/josua/Downloads")
            print("mv " + file + " /home/josua/uni/ex/zettel")
            os.system("mv " + file + " /home/josua/uni/ex/zettel")

#tuesday and thursday evening
def get_la1_skript():
    os.system("firefox -new-tab 'https://mampf.mathi.uni-heidelberg.de/courses/1/food?lecture_id=11&project=script'")
    time.sleep(5)
    os.system("xdotool key Ctrl+s")
    time.sleep(1)
    os.system("xdotool key Return")
    time.sleep(3)
    os.system("xdotool key Ctrl+w")
    with open("/home/josua/Downloads/MaMpf.html") as f:
        lines = f.readlines()
    os.system("rm -rf /home/josua/Downloads/MaMpf-Dateien")
    os.system("rm /home/josua/Downloads/MaMpf.html")
    text = ""
    for line in lines:
        text += line
    soup = BeautifulSoup(text, "html.parser")
    body = soup.body
    divlist = body.find_all('div')
    downloadstuff = []
    for div in divlist:
        try:
            if "download-button" in div["class"]:
                downloadstuff.append(div)
        except:
            pass
    downloaddict = {}
    for div in downloadstuff:
        a = div.a
        name = a["download"][-10:]
        link = a["href"]
        downloaddict[name] = link
    for name in downloaddict:
        link = downloaddict[name]
        splitlink = link.split("/")
        uglyfilename = splitlink[-1]
        os.system("firefox -new-tab "+link)
        time.sleep(1)
        os.system("xdotool key Ctrl+w")
        time.sleep(1)
        command1 = "mv /home/josua/Downloads/" + uglyfilename + " /home/josua/uni/la/skripte/" + name
        print(command1)
        os.system(command1)

#thursday evening
def get_la1_zettel():
    os.system("firefox -new-tab 'https://mampf.mathi.uni-heidelberg.de/courses/1/food?lecture_id=11&project=nuesse'")
    time.sleep(2)
    os.system("xdotool key Ctrl+s")
    time.sleep(2)
    os.system("xdotool key Return")
    time.sleep(2)
    os.system("xdotool key Ctrl+w")
    with open("/home/josua/Downloads/MaMpf.html") as f:
        lines = f.readlines()
    os.system("rm -rf /home/josua/Downloads/MaMpf-Dateien")
    os.system("rm /home/josua/Downloads/MaMpf.html")
    text = ""
    for line in lines:
        text += line
    soup = BeautifulSoup(text, "html.parser")
    body = soup.body
    divlist = body.find_all('div')
    downloadstuff = []
    for div in divlist:
        try:
            if "download-button" in div["class"]:
                downloadstuff.append(div)
        except:
            pass
    downloaddict = {}
    for div in downloadstuff:
        a = div.a
        name = a["download"][-6:]
        link = a["href"]
        downloaddict[name] = link
    #already in folder uni/la/zettel
    alreadydownloaded = os.listdir("/home/josua/uni/la/zettel")
    newstuff = []
    for name in downloaddict:
        if name not in alreadydownloaded:
            newstuff.append(name)
    for name in newstuff:
        link = downloaddict[name]
        splitlink = link.split("/")
        uglyfilename = splitlink[-1]
        os.system("firefox -new-tab "+link)
        time.sleep(1)
        os.system("xdotool key Ctrl+w")
        time.sleep(1)
        command1 = "mv /home/josua/Downloads/" + uglyfilename + " /home/josua/uni/la/zettel/" + name
        os.system(command1)

def get_ipi_zettel():
    alreadydownloaded = os.listdir("~/uni/ipi/zettel")
    soup = get_soup('https://conan.iwr.uni-heidelberg.de/teaching/info1_ws2019/')
    divlist = soup.find_all('div')
    for div in divlist:
        try:
            if "panel-body" in div["class"]:
                main = div
                break
        except:
            pass
    fatlist = main.find_all('h2')
    for element in fatlist:
        try:
            if "übungsblätter" in element["id"]:
                zettelmain = element
                break
        except:
            pass
    zettelliste = zettelmain.find_all("p")
    for zettel in zettelliste:
        pass


#monday
#get_ex1_content()
#get_theo1_zettel()

#tuesday
#get_la1_skript()
#future: ipi

#wednesday
#get_ex1_content()

#thursday
get_ex1_zettel()
#get_la1_skript()
#get_la1_zettel()
