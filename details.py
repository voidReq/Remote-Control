import os
import platform
from getmac import get_mac_address as gma
import socket
import urllib.request


"""https://cdn.discordapp.com/attachments/101207951445352518/1131062228930543656"""
format = "---------------------------------------------------"
directory = os.getcwd()


def detailGetter():
  hostname = socket.gethostname()
  privateIP = socket.gethostbyname(hostname)
  publicIP = external_ip = urllib.request.urlopen(
      'https://ident.me').read().decode('utf8')
  mac = gma()
  user = os.getlogin()
  system = platform.system()
  release = platform.release()
  version = platform.version()

  allAtOnce = f"""
Hostname: {hostname}
{format}
Public IP Address: {publicIP}
{format}
Private IP Address: {privateIP}
{format}
Mac address: {mac}
{format}
User: {user}
{format}
OS info: \n---{system}\n---{release}\n---{version}
{format}
CWD: {os.getcwd()}
{format}
"""
  return(allAtOnce)

