import subprocess
import os
import sys
os.system("sudo apt-get update")
os.system("sudo dpkg --add-architecture i386 && apt-get update")
os.system("sudo apt-get install wine -y && apt-get install wine32 -y")
os.system("sudo apt-get install figlet -y")
os.system("pip install opencv-python")
hostname=subprocess.check_output("hostname",shell=True)
hostname=hostname.split("\n")
os.system("wine msiexec /i python/python-2.7.17.amd64.msi")
pywin32_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install pywin32"
os.system(pywin32_installer)
pyautogui_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install pyautogui"
os.system(str(pyautogui_installer))
opencv_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install opencv-python"
os.system(opencv_installer)
sounddevice_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install sounddevice"
os.system(sounddevice_installer)
requests_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install requests"
os.system(requests_installer)
pynput_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install pynput"
os.system(pynput_installer)
cryptography_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install cryptography"
os.system(cryptography_installer)
scipy_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install scipy"
os.system(scipy_installer)
pyinstaller_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install pyinstaller"
os.system(pyinstaller_installer)
pywin32_ctypes_installer="wine /home/"+str(hostname[0])+"/.wine/drive_c/Python27/Scripts/pip.exe install pywin32-ctypes"
os.system(pywin32_ctypes_installer)
