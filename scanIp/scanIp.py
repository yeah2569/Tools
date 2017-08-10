import time
import threading
import socket

threads = []

def get_hostname(ip):
    try:
        (name, aliaslist, addresslist) = socket.gethostbyaddr(ip)
        print name , '  ', ip
                
    except Exception as e:
        return
    
      
def find_ip(ip_prefix):  
       
    for i in range(2,255):  
        ip = '%s.%s'%(ip_prefix,i)
        th=threading.Thread(target=get_hostname,args=(ip,))
        threads.append(th)
  
    
if __name__ == "__main__":  
    print "start time %s"%time.ctime()  
    
    find_ip('192.168.2')  
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()   

    print "end time %s"%time.ctime()  