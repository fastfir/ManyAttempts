import os
def attempt(ip):
    os.system("timeout 5 ftp " + ip)
    os.system("anonymous")
    
