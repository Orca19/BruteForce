from socket import *
import hashlib
import time
ser_soc = socket()
ser_soc.bind(('192.168.1.102',52000))
ser_soc.listen(2)
s,addr = ser_soc.accept()
mes = s.recv(1024).decode()
if mes=='amogus':
    s.send('01'.encode())
    time.sleep(0.1)
    print("duck")
    mes = s.recv(1024).decode()
    if mes=='01':  
        MD5 = hashlib.md5(("abg").encode()).hexdigest()
        data = 'start:aaa,stop:zzz,MD5:'+MD5
        s.send(data.encode())
        mes = s.recv(1024).decode()
        if mes=='ok':
            print("recieved ok")
            mes = s.recv(1024).decode()
            s.send(("got password "+mes).encode())
            time.sleep(5)

ser_soc.close()

