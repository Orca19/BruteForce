def BruteForce(start_phrase, stop_phrase, list, MD5, passwords_LIST):
    import pandas as pd
    import hashlib


    while True:
        password = ''.join(list)
        password_md5 = hashlib.md5(password.encode('UTF-8')).hexdigest()
        if password_md5==MD5:
            return password
        passwords_LIST[0].append(password)
        passwords_LIST[1].append(password_md5)
        if  ''.join(list)==stop_phrase:
            return 'password was not found'
            
        i = -1
        while list[i]==stop_phrase[0]:
            list[i] = start_phrase[0]
            i-=1   
        list[i] = chr(ord(list[i])+1)
    """
    if ''.join(list)==stop_phrase:
        print("password wasn't found")


    password_tab = {}
    password_tab['passwords'] = passwords_LIST[0]
    password_tab['MD5'] = passwords_LIST[1]
    df = pd.DataFrame.from_dict(password_tab)
    print(df)
    """

def main():
    """
    import threading
    passwords_LIST =[[],[]]
    start_phrase = input("Enter start phrase ")
    stop_phrase  = input("Enter stop phrase ")
    MD5 = input("Enter MD5 ")
    list = [chr for chr in start_phrase]
    BruteForce(start_phrase, stop_phrase, list, MD5, passwords_LIST)
    """
    """
    dif = ord(stop_phrase[0])-ord(start_phrase[0])
    if dif<=50:
        n=1
    elif dif>50 and dif<75:
        n=2

    else:
        n=3
    threads = []
    start = start_phrase
    stop = start
    for i in range(n):
        if i==n-1:
            stop = stop_phrase
        else:
            start =chr((ord(stop[0])+1))*len(start_phrase)
            stop = chr((ord(stop[0])+dif//n))*len(start_phrase)
        list = [chr for chr in start]
        t = threading.Thread(target=BruteForce, args = (start, stop, list, MD5, passwords_LIST))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
        """

if __name__ =='__main__':
    main()


