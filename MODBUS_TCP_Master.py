import socket
import struct

TCP_IP = '192.168.1.101'
PORT = 502

master = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
master.connect((TCP_IP,PORT))

try:
    unitId = 16
    functionCode = 5
    req = struct.pack('12B',0x00,0x00,0x00,0x00,0x00,0x06,
                      0x01,0x03,0x00,0x00,0x00,0x01)
    print('TO:',req)
    master.send(req)
    data = master.recv(1024)
    print(data)
    
    str_data = str(data)
    print(str_data[-3:-1])
    

finally:
    master.close()
    print('modbus tcp is closs')
