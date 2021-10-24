import msvcrt
import socket

    #TCP SETUP#
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

    #MAIN LOOP#
while(1):
    key =  msvcrt.getch()                   #read keyboard input

    s.send(key)                             #send keyboard input to rover
    data = s.recv(BUFFER_SIZE)
    print ("received data:", data)

    if key == b'p':break                    #terminate program in 'p' is pressed
s.close()
   
