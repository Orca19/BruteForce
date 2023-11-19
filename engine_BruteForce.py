from socket import *
import time
import BruteForceV2
soc = socket()
addr = ('0,0,0,0', 2222)
soc.connect(addr)
data = 'amogus'
soc.send(data.encode('uf-8'))
time.sleep(0.1)
answer  = soc.recv(1024).decode('utf-8')
soc.send(answer.encode('utf-8'))
time.sleep(0.1)
while True:
    answer  = soc.recv(1024).decode('utf-8')
    time.sleep(0.1)
    soc.send('ok'.encode('utf-8'))
    inputs = answer.split(',')
    start = inputs[0][6:]
    stop = inputs[1][5:]
    MD5 = input[2][4:]
    start_list = [chr for chr in start]
    password = BruteForceV2.BruteForce(start, stop,start_list, MD5)
    if password!='password was not found':
        answer = 'success '
    else:
        answer = 'failed '
    answer+=password
    soc.send(answer.encode('utf-8'))
    answer  = soc.recv(1024).decode('utf-8')
    soc.send('next'.encode('utf-8'))




