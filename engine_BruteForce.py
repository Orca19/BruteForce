from socket import *
import time
import communication

global end 
end = False

soc = socket()
addr = ('192.168.1.102', 52000)
soc.connect(addr)
print("connected")
data = 'amogus'
soc.send(data.encode('utf-8'))
print("sent word")
time.sleep(0.1)
answer  = soc.recv(1024).decode('utf-8')
print("recieved word")
soc.send(answer.encode('utf-8'))
time.sleep(0.1)
print("entering communication")
communication.main(soc,end)





