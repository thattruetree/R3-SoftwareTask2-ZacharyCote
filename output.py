import socket
 
speed = 0               # speed initially set to zero

    #TCP SETUP#
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connection address:', addr)


    #Main Loop#
while 1:
    data = conn.recv(BUFFER_SIZE)       #receive keyboard input
    print( "received data:", data)
    if data == b'p':break               #Terminates loop when signal received is 'p'


    #SPEED SETTINGS#
    if data == b'0':                    #Sets spped to 0
        speed = 0
        print('Speed set to 0')  
    if data == b'1':                    #Sets spped to 1
        speed = 255*0.2
        print('Speed set to 1 (20%)')   
    if data == b'2':                    #Sets spped to 2
        speed = 255*0.4
        print('Speed set to 2 (40%)')  
    if data == b'3':                    #Sets spped to 3
        speed = 255*0.6
        print('Speed set to 3 (60%))')  
    if data == b'4':                    #Sets spped to 4
        speed = 255*0.8
        print('Speed set to 4 (80%)')  
    if data == b'5':                     #Sets spped to 5
        speed = 255
        print('Speed set to 5 (MAX)')  



    #MOTOR DRIVE COMMANDS#
    if data == b'w':                                                 #drive forward
        print('[f',speed,'][f',speed,'][f',speed,'][f', speed,']')  
    if data == b'a':                                                 #turn left
        print('[r',speed,'][r',speed,'][f',speed,'][f', speed,']')
    if data == b's':                                                 #drive backwards
        print('[r',speed,'][r',speed,'][r',speed,'][r', speed,']') 
    if data == b'd':                                                 #turn right
        print('[f',speed,'][f',speed,'][r',speed,'][r', speed,']')
  

    conn.send(data)  # send keypress back to client to comfirm it was processed by the server
conn.close()