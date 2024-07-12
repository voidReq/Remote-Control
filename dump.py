from details import detailGetter
from wifi import wifiSnatch

f = open("file269446.txt", "a")
f.write(detailGetter())
f.write(wifiSnatch())
f.close()

