from socket import *
import time
import communication

global end 
end = False

soc = socket()
addr = ('192.168.1.102', 52000)
soc.connect(addr)
print("connected to server")
data = 'amogus'
soc.send(data.encode('utf-8'))
print("sent key word")
time.sleep(0.1)
answer  = soc.recv(1024).decode('utf-8')
print("recieved number")
soc.send(answer.encode('utf-8'))
print("sending number back")
time.sleep(0.1)
print("entering communication")
communication.main(soc,end)





