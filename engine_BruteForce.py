from socket import *
import time
import communication

global end 
end = False

soc = socket()
addr = ('0,0,0,0', 2222)
soc.connect(addr)
data = 'amogus'
soc.send(data.encode('uf-8'))
time.sleep(0.1)
answer  = soc.recv(1024).decode('utf-8')
soc.send(answer.encode('utf-8'))
time.sleep(0.1)

communication.main(soc,end)





