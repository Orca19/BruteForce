from socket import *
import time
import BruteForceV2
import threading


def blocking(soc, end):
    answer1  = soc.recv(1024).decode('utf-8')
    if answer1=='end':
        end = True
        
def com(soc, end):
    while not end:
        answer  = soc.recv(1024).decode()
        if answer[:6]=='start:':
            time.sleep(0.1)
            soc.send('ok'.encode('utf-8'))
            print("got data")
            inputs = answer.split(',')
            start = inputs[0][6:]
            stop = inputs[1][5:]
            MD5 = inputs[2][4:]
            start_list = [chr for chr in start]
            password = BruteForceV2.BruteForce(start, stop,start_list, MD5)
            if password!='password was not found':
                answer = 'success '
            else:
                answer = 'failed '
            answer+=password
            print(password)
            soc.send(answer.encode('utf-8'))
            print("password was sent")
            time.sleep(0.1)
            answer  = soc.recv(1024).decode('utf-8')
            print(answer)
            if answer!='ok':
                break
            soc.send('next'.encode('utf-8'))
    soc.close()
def main(soc, end):
    threads = []
    t1 = threading.Thread(target = com, args = (soc,end))
    t2 = threading.Thread(target = blocking, args = (soc,end))
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.start()
    print("started threads")

if __name__ =='__main__':
    main()